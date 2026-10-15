"""Gemini Builder skill bundle structure, provenance and negative tests."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from zipfile import ZipFile

AUTOMATION = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AUTOMATION))
import build_gemini_skill as gemini  # noqa: E402
import platform_skill_common as common  # noqa: E402


class GeminiSkillTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = gemini.build_files()
        cls.map = json.loads(cls.files["references/SOURCE_MAP.json"])

    def test_gemini_frontmatter_is_exactly_expected_keys(self):
        text = self.files["SKILL.md"].decode("utf-8")
        common.check_frontmatter(text)
        self.assertTrue(text.startswith("---\nname: aio-ai-builder\n"))
        self.assertIn("assistant-building tasks", text)

    def test_38_verbatim_canonical_sources(self):
        entries = self.map["source_files"]
        self.assertEqual(38, len(entries))
        self.assertEqual(9, sum(x["role"] == "builder-design-reference" for x in entries))
        self.assertEqual(22, sum(x["role"] == "target-runtime-module-reference" for x in entries))
        self.assertEqual(4, sum(x["role"] == "target-runtime-contract-reference" for x in entries))
        for entry in entries:
            with self.subTest(source=entry["source"]):
                original = common.read_source(entry["source"])
                self.assertEqual(original, self.files[entry["bundled"]])
                self.assertEqual(common.sha256(original), entry["sha256"])

    def test_adapter_metadata_separate_from_runtime_manifest(self):
        self.assertEqual("gemini", self.map["adapter"])
        self.assertEqual("0.1.3-dev", self.map["adapter_version"])
        self.assertEqual("reference-only-for-generated-assistants", self.map["runtime_material_use"])
        manifest = json.loads(self.files["references/runtime/01_MANIFEST.json"])
        self.assertEqual(manifest, json.loads(common.read_source("package/01_MANIFEST.json")))

    def test_skill_is_builder_not_runtime(self):
        content = self.files["SKILL.md"].decode("utf-8")
        contract = self.files["references/BUILDER_CONTRACT.md"].decode("utf-8")
        self.assertIn("Do not activate it for ordinary research", content)
        self.assertIn("never recommend blindly appending", content.lower() + " " + contract.lower())
        self.assertIn("existing assistant", content.lower())
        self.assertIn("GM-09", content)
        self.assertIn("SM-04", content)
        self.assertIn("GM-04", content)
        self.assertIn("GM-02", content)
        self.assertIn("GM-08", content)
        self.assertIn("runtime", content)
        self.assertIn("A recommended tool does not mean it is installed or was used", contract)

    def test_no_private_material_scripts_or_binaries_in_installables(self):
        self.assertEqual(43, len(self.files))
        for name in self.files:
            self.assertTrue(name == "SKILL.md" or name.startswith("references/"), name)
            self.assertTrue(name.endswith((".md", ".json", ".txt")), name)
            for blocked in (".git/", ".gitea/", ".github/", "tests/", "automation/", ".env", "results/", "architecture/"):
                self.assertNotIn(blocked, name)
        self.assertNotIn("knowledge/09_Changelog.md", [x["source"] for x in self.map["source_files"]])

    def test_relative_links_resolve(self):
        common.validate_paths(self.files)
        self.assertIn("references/runtime/modules/governing/GM-09_Specialized_Response_Patterns.md", self.files)

    def test_apps_zip_has_root_skill(self):
        with tempfile.TemporaryDirectory() as td:
            artifacts = gemini.build_artifacts(Path(td))
            with ZipFile(artifacts["apps"]) as z:
                names = z.namelist()
                self.assertIn("SKILL.md", names)
                self.assertNotIn("aio-ai-builder/SKILL.md", names)
                self.assertEqual(set(names), set(self.files))
                self.assertIsNone(z.testzip())

    def test_cli_skill_has_named_folder(self):
        with tempfile.TemporaryDirectory() as td:
            artifacts = gemini.build_artifacts(Path(td))
            with ZipFile(artifacts["cli"]) as z:
                names = z.namelist()
                self.assertIn("aio-ai-builder/SKILL.md", names)
                self.assertNotIn("SKILL.md", names)
                self.assertEqual({"aio-ai-builder/" + s for s in self.files}, set(names))
                self.assertIsNone(z.testzip())
            self.assertEqual(".skill", artifacts["cli"].suffix)

    def test_checksum_matches_both_artifacts(self):
        with tempfile.TemporaryDirectory() as td:
            for path in gemini.build_artifacts(Path(td)).values():
                file, name = Path(str(path) + ".sha256"), path.name
                self.assertTrue(file.is_file())
                self.assertEqual(file.read_text().strip(), f"{common.sha256(path.read_bytes())}  {name}")

    def test_both_archives_byte_reproducible(self):
        with tempfile.TemporaryDirectory() as td:
            a = gemini.build_artifacts(Path(td) / "a")
            b = gemini.build_artifacts(Path(td) / "b")
            for form in ("apps", "cli"):
                self.assertEqual(a[form].read_bytes(), b[form].read_bytes())

    def test_missing_required_source_aborts(self):
        original = common.read_source
        def missing(path):
            if path == "knowledge/02_Instruction_Building_Blocks.md":
                raise common.BuildError("Required file missing")
            return original(path)
        with patch.object(common, "read_source", side_effect=missing):
            with self.assertRaises(common.BuildError):
                gemini.build_files()

    def test_private_extra_source_in_map_aborts(self):
        original = common.read_source
        def added(path):
            content = original(path)
            if path == "platforms/shared/REFERENCE_MAP.json":
                obj = json.loads(content)
                obj["files"].append({"source": "architecture/01_V1_Concept_Inventory.md",
                                     "target": "references/builder/private.md", "role": "builder-design-reference"})
                return json.dumps(obj).encode("utf-8")
            return content
        with patch.object(common, "read_source", side_effect=added):
            with self.assertRaisesRegex(common.BuildError, "drift"):
                gemini.build_files()

    def test_manifest_module_change_aborts(self):
        original = common.read_source
        def changed(path):
            content = original(path)
            if path == "package/01_MANIFEST.json":
                obj = json.loads(content)
                obj["modules"]["governing"].pop()
                return json.dumps(obj).encode("utf-8")
            return content
        with patch.object(common, "read_source", side_effect=changed):
            with self.assertRaisesRegex(common.BuildError, r"11\+11"):
                gemini.build_files()

    def test_unknown_frontmatter_field_aborts(self):
        modified = dict(self.files)
        modified["SKILL.md"] = modified["SKILL.md"].replace(b"name: aio-ai-builder\n", b"name: aio-ai-builder\nversion: 99\n")
        with self.assertRaises(common.BuildError):
            common.validate_paths(modified)

    def test_invalid_relative_link_aborts(self):
        modified = dict(self.files)
        modified["SKILL.md"] = modified["SKILL.md"].replace(b"references/BUILDER_CONTRACT.md", b"references/nonexistent.md")
        with self.assertRaisesRegex(common.BuildError, "Broken skill link"):
            common.validate_paths(modified)

    def test_unsafe_paths_aborts(self):
        for bad in ("../secrets.txt", "/tmp/x", "references/../private", "references/.env", "references\\secret.md"):
            with self.subTest(bad=bad), self.assertRaises(common.BuildError):
                common.safe_relative(bad)

    def test_unsupported_versions_abort(self):
        for bad in ("1.0.0-rc.x", "../../a", "v1.0.0", "", "1.0.0;echo"):
            with self.subTest(version=bad), self.assertRaises(common.BuildError):
                gemini.build_files(bad)

    def test_malformed_reference_entry_aborts(self):
        original = common.read_source
        def malformed(path):
            content = original(path)
            if path == "platforms/shared/REFERENCE_MAP.json":
                obj = json.loads(content)
                obj["files"][0]["role"] = "malicious-instruction"
                return json.dumps(obj).encode("utf-8")
            return content
        with patch.object(common, "read_source", side_effect=malformed):
            with self.assertRaisesRegex(common.BuildError, "Wrong source role"):
                gemini.build_files()


if __name__ == "__main__":
    unittest.main()
