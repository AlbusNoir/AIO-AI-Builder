"""Deterministic Phase 2 checks for AIO AI Builder's Claude reference skill."""

from __future__ import annotations

import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from zipfile import ZipFile

SCRIPT = Path(__file__).resolve().parents[1] / "build_claude_skill.py"
SPEC = importlib.util.spec_from_file_location("build_claude_skill", SCRIPT)
builder = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(builder)


class ClaudeSkillTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = builder.build_files()
        builder.validate_paths(cls.files)
        cls.map = json.loads(cls.files["references/SOURCE_MAP.json"])

    def test_frontmatter_name_and_short_description(self):
        text = self.files["SKILL.md"].decode("utf-8")
        builder.check_skill_frontmatter(text)
        self.assertTrue(text.startswith("---\nname: aio-ai-builder\n"))
        self.assertIn("assistant-building requests", text)

    def test_source_inventory_and_reference_roles(self):
        source_files = self.map["source_files"]
        self.assertEqual(38, len(source_files))
        self.assertEqual(9, sum(x["role"] == "builder-design-reference" for x in source_files))
        self.assertEqual(22, sum(x["role"] == "target-runtime-module-reference" for x in source_files))
        self.assertEqual(4, sum(x["role"] == "target-runtime-contract-reference" for x in source_files))
        self.assertEqual("reference-only-for-generated-assistants", self.map["runtime_material_use"])

    def test_verbatim_canonical_source_bytes_and_hashes(self):
        for item in self.map["source_files"]:
            with self.subTest(source=item["source"]):
                original = builder.read_source(item["source"])
                bundled = self.files[item["bundled"]]
                self.assertEqual(original, bundled)
                self.assertEqual(builder.sha256(original), item["sha256"])

    def test_no_private_repository_material(self):
        self.assertTrue(all(x == "SKILL.md" or x.startswith("references/") for x in self.files))
        forbidden = ("tests/", "automation/", ".git/", ".gitea/", ".github/", ".env", "architecture/", "results/")
        for path in self.files:
            for marker in forbidden:
                self.assertNotIn(marker, path)
        self.assertNotIn("knowledge/09_Changelog.md", [x["source"] for x in self.map["source_files"]])

    def test_generated_links_resolve(self):
        builder.validate_paths(self.files)
        self.assertIn("references/runtime/modules/governing/GM-02_Knowledge_Source_Handling.md", self.files)

    def test_archive_root_layout_and_hash(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "skill.zip"
            digest = builder.make_zip(path, self.files)
            self.assertEqual(builder.sha256(path.read_bytes()), digest)
            with ZipFile(path) as z:
                names = z.namelist()
                self.assertEqual(len(names), len(self.files))
                self.assertIn("aio-ai-builder/SKILL.md", names)
                self.assertNotIn("SKILL.md", names)
                self.assertTrue(all(n.startswith("aio-ai-builder/") for n in names))
                self.assertTrue(z.testzip() is None)

    def test_build_is_byte_reproducible(self):
        with tempfile.TemporaryDirectory() as td:
            a, b = Path(td) / "a.zip", Path(td) / "b.zip"
            builder.make_zip(a, self.files)
            builder.make_zip(b, builder.build_files())
            self.assertEqual(a.read_bytes(), b.read_bytes())

    def test_missing_canonical_file_is_fatal(self):
        original = builder.read_source
        def missing(path):
            if path == "knowledge/01_Design_Principles.md":
                raise builder.BuildError("Required canonical source missing")
            return original(path)
        with patch.object(builder, "read_source", side_effect=missing):
            with self.assertRaises(builder.BuildError):
                builder.build_files()

    def test_extra_private_file_refused_even_if_added_to_allowlist(self):
        original = builder.read_source
        def modified(path):
            content = original(path)
            if path == "platforms/shared/REFERENCE_MAP.json":
                data = json.loads(content)
                data["files"].append({"source":"architecture/01_V1_Concept_Inventory.md",
                                     "target":"references/builder/extra.md", "role":"builder-design-reference"})
                return json.dumps(data).encode("utf-8")
            return content
        with patch.object(builder, "read_source", side_effect=modified):
            with self.assertRaisesRegex(builder.BuildError, "allowlist differs"):
                builder.build_files()

    def test_manifest_inventory_drift_is_fatal(self):
        original = builder.read_source
        def altered(path):
            content = original(path)
            if path == "package/01_MANIFEST.json":
                data = json.loads(content)
                data["modules"]["governing"].pop()
                return json.dumps(data).encode("utf-8")
            return content
        with patch.object(builder, "read_source", side_effect=altered):
            with self.assertRaises(builder.BuildError):
                builder.build_files()

    def test_unexpected_version_refused(self):
        for version in ("../1.0.0", "v1.0.0", "1.0.0-rc.x", "0.1.0;rm", ""):
            with self.subTest(version=version), self.assertRaises(builder.BuildError):
                builder.build_files(version)

    def test_invalid_skills_link_rejected(self):
        bad = dict(self.files)
        bad["SKILL.md"] = bad["SKILL.md"].replace(b"references/BUILDER_INDEX.md", b"references/not-present.md")
        with self.assertRaisesRegex(builder.BuildError, "Broken bundled link"):
            builder.validate_paths(bad)

    def test_existing_assistant_requires_source_aware_revision(self):
        contract = self.files["references/BUILDER_CONTRACT.md"].decode("utf-8")
        skill = self.files["SKILL.md"].decode("utf-8")
        for phrase in (
            "inspect its actual instructions",
            "canonical owners",
            "provisional example",
            "never tell the user to append an unreviewed patch",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, contract)
        self.assertIn("do not suggest blindly appending instructions", skill)

    def test_existing_assistant_delivery_not_claimed_compatible_without_source(self):
        output = self.files["references/OUTPUT_CONTRACT.md"].decode("utf-8")
        self.assertIn("unverified for integration", output)
        self.assertIn("one complete reconciled instruction set", output)
        self.assertIn("do not recommend blindly appending", output)

    def test_specialized_response_pattern_ownership(self):
        contract = self.files["references/BUILDER_CONTRACT.md"].decode("utf-8")
        skill = self.files["SKILL.md"].decode("utf-8")
        self.assertIn("GM-09 owns substantive, task-specific work-product/response architecture", contract)
        self.assertIn("SM-04 may refine presentation", contract)
        self.assertIn("GM-09 (specialized response architecture) distinct from SM-04 (presentation)", skill)

    def test_source_and_research_ownership_are_distinct(self):
        contract = self.files["references/BUILDER_CONTRACT.md"].decode("utf-8")
        skill = self.files["SKILL.md"].decode("utf-8")
        self.assertIn("GM-04 owns external discovery/research", contract)
        self.assertIn("GM-02 owns source treatment, authority, provenance", contract)
        self.assertIn("GM-08 owns an *explicitly bounded source mode*", contract)
        self.assertIn("Approved source lists alone do not make every research workflow", contract)
        self.assertIn("GM-04 (external research), GM-02 (source treatment), and GM-08", skill)

    def test_capability_integrity_still_required(self):
        contract = self.files["references/BUILDER_CONTRACT.md"].decode("utf-8")
        self.assertIn("A recommended tool does not mean it is installed or was used", contract)
        self.assertIn("never create fabricated provenance", contract)

    def test_refined_dev_version(self):
        self.assertEqual("0.1.3-dev", builder.DEFAULT_VERSION)
        self.assertEqual("0.1.3-dev", self.map["adapter_version"])

    def test_no_unconditional_runtime_role(self):
        skill = self.files["SKILL.md"].decode("utf-8")
        self.assertIn("Runtime module reference files are design templates", skill)
        self.assertIn("Do not blindly load or impose all modules", skill)
        self.assertIn("ordinary domain task", skill)


if __name__ == "__main__":
    unittest.main()
