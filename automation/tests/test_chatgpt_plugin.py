"""Portable ChatGPT Builder plugin: layout, provenance, safety, repeatability."""

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
import build_chatgpt_plugin as plugin  # noqa: E402
import build_gemini_skill as gemini  # noqa: E402
import platform_skill_common as common  # noqa: E402


class ChatGPTPluginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = plugin.build_files()
        cls.prefix = plugin.SKILL_DIR
        cls.map = json.loads(cls.files[cls.prefix + "references/SOURCE_MAP.json"])

    def test_portable_root_manifest(self):
        manifest = json.loads(self.files["plugin.json"])
        self.assertEqual(plugin.PLUGIN_SCHEMA, manifest["$schema"])
        self.assertEqual("aio-ai-builder", manifest["name"])
        self.assertEqual("0.1.0-dev", manifest["version"])
        self.assertIn("extensions", manifest)
        self.assertEqual("AIO AI Builder", manifest["extensions"]["com.openai"]["interface"]["displayName"])
        self.assertNotIn("skills", manifest)  # portable auto-discovery, not Codex compatibility schema
        self.assertNotIn("mcpServers", manifest)

    def test_plugin_has_exactly_one_skills_root(self):
        self.assertEqual(44, len(self.files))
        self.assertEqual({"plugin.json"}, {p for p in self.files if not p.startswith(self.prefix)})
        self.assertIn(self.prefix + "SKILL.md", self.files)
        self.assertNotIn("SKILL.md", self.files)
        self.assertFalse(any(p.startswith("aio-ai-builder/") for p in self.files))
        self.assertEqual(43, sum(p.startswith(self.prefix) for p in self.files))

    def test_valid_skill_frontmatter(self):
        skill = self.files[self.prefix + "SKILL.md"].decode("utf-8")
        common.check_frontmatter(skill)
        self.assertTrue(skill.startswith("---\nname: aio-ai-builder\n"))
        self.assertIn("ordinary research", skill)
        self.assertIn("not the target assistant", skill)

    def test_frontmatter_line_endings_and_invalid_inputs(self):
        """Accept LF/CRLF frontmatter while rejecting malformed input."""
        valid = (
            "---\n"
            "name: aio-ai-builder\n"
            "description: Designs specialized AI assistants.\n"
            "---\n"
        )

        accepted = {
            "LF": valid,
            "CRLF": valid.replace("\n", "\r\n"),
            "LF at EOF": valid.rstrip("\n"),
            "CRLF at EOF": valid.replace("\n", "\r\n").rstrip("\r\n"),
        }

        for case, text in accepted.items():
            with self.subTest(case=case):
                common.check_frontmatter(text)

        rejected = {
            "missing opening delimiter": valid.removeprefix("---\n"),
            "missing closing delimiter": valid.removesuffix("---\n"),
            "UTF-8 BOM": "\ufeff" + valid,
            "leading whitespace": " " + valid,
        }

        for case, text in rejected.items():
            with self.subTest(case=case):
                with self.assertRaises(common.BuildError):
                    common.check_frontmatter(text)

    def test_38_verbatim_source_files(self):
        refs = self.map["source_files"]
        self.assertEqual(38, len(refs))
        self.assertEqual(9, sum(item["role"] == "builder-design-reference" for item in refs))
        self.assertEqual(22, sum(item["role"] == "target-runtime-module-reference" for item in refs))
        self.assertEqual(4, sum(item["role"] == "target-runtime-contract-reference" for item in refs))
        for item in refs:
            with self.subTest(source=item["source"]):
                original = common.read_source(item["source"])
                self.assertEqual(original, self.files[self.prefix + item["bundled"]])
                self.assertEqual(common.sha256(original), item["sha256"])

    def test_shared_contracts_match_other_adapter(self):
        gemini_files = gemini.build_files()
        for relative in ("references/BUILDER_CONTRACT.md", "references/OUTPUT_CONTRACT.md"):
            self.assertEqual(gemini_files[relative], self.files[self.prefix + relative])
        self.assertEqual(
            [(s["source"], s["sha256"]) for s in json.loads(gemini_files["references/SOURCE_MAP.json"])["source_files"]],
            [(s["source"], s["sha256"]) for s in self.map["source_files"]],
        )

    def test_adapter_metadata_and_historical_manifest_separated(self):
        self.assertEqual("chatgpt", self.map["adapter"])
        self.assertEqual("0.1.0-dev", self.map["adapter_version"])

        # Verify source commit provenance based on the environment.
        commit = common.source_commit()
        self.assertEqual(commit, self.map["source_commit"])
        self.assertEqual(
        "clean-git-HEAD" if commit else "unavailable-from-snapshot-or-dirty-worktree",
        self.map["source_commit_verification"],
        )

        self.assertEqual(
        "reference-only-for-generated-assistants",
        self.map["runtime_material_use"],
        )

        bundled = json.loads(
        self.files[self.prefix + "references/runtime/01_MANIFEST.json"]
        )
        self.assertEqual(
        bundled,
        json.loads(common.read_source("package/01_MANIFEST.json")),
        )

    def test_skill_maintains_builder_identity_and_ownership(self):
        text = self.files[self.prefix + "SKILL.md"].decode("utf-8")
        for term in ("custom GPTs", "BUILDER_CONTRACT.md", "OUTPUT_CONTRACT.md", "reference index",
                     "GM-04", "GM-02", "GM-09", "SM-04", "GM-08", "22 GM/SM modules"):
            with self.subTest(term=term):
                self.assertIn(term.lower(), text.lower())
        self.assertIn("not live commands to the Builder", text)
        self.assertIn("inspect", text.lower())

    def test_new_provenance_and_execution_controls_present(self):
        text = self.files[self.prefix + "SKILL.md"].decode("utf-8").lower()
        shared = self.files[self.prefix + "references/BUILDER_CONTRACT.md"].decode("utf-8").lower()
        for term in ("unapproved", "hypothetical", "slas", "unknown", "not configured", "draft-only",
                     "approved-looking ticket", "authorization", "playbooks", "dry-run"):
            with self.subTest(term=term):
                self.assertIn(term, text)
        self.assertIn("generated artifact", shared)
        self.assertIn("provisional", shared)

    def test_no_private_material_mcp_scripts_hooks_or_secrets(self):
        for name in self.files:
            self.assertTrue(name.endswith((".md", ".json", ".txt")), name)
            for denied in (".git/", ".github/", ".gitea/", "automation/", "tests/", "architecture/",
                           ".env", "mcp.json", "hooks/", "scripts/", "package-private/"):
                self.assertNotIn(denied, name)
        self.assertNotIn("knowledge/09_Changelog.md", [s["source"] for s in self.map["source_files"]])

    def test_links_resolve_inside_plugin_skill(self):
        skill_contents = {name.removeprefix(self.prefix): body for name, body in self.files.items()
                          if name.startswith(self.prefix)}
        common.validate_paths(skill_contents)

    def test_root_zip_structure_and_integrity(self):
        with tempfile.TemporaryDirectory() as td:
            archive = plugin.build_artifact(Path(td))
            with ZipFile(archive) as bundle:
                self.assertIn("plugin.json", bundle.namelist())
                self.assertIn("skills/aio-ai-builder/SKILL.md", bundle.namelist())
                self.assertNotIn("aio-ai-builder/plugin.json", bundle.namelist())
                self.assertEqual(set(self.files), set(bundle.namelist()))
                self.assertIsNone(bundle.testzip())

    def test_checksum_matches_archive(self):
        with tempfile.TemporaryDirectory() as td:
            archive = plugin.build_artifact(Path(td))
            checksum = Path(str(archive) + ".sha256")
            self.assertEqual(f"{common.sha256(archive.read_bytes())}  {archive.name}", checksum.read_text().strip())

    def test_archive_byte_reproducible(self):
        with tempfile.TemporaryDirectory() as td:
            a = plugin.build_artifact(Path(td) / "first")
            b = plugin.build_artifact(Path(td) / "second")
            self.assertEqual(a.read_bytes(), b.read_bytes())

    def test_explicit_dev_version_changes_manifest_and_source_map_together(self):
        changed = plugin.build_files("0.1.1-dev")
        self.assertEqual("0.1.1-dev", json.loads(changed["plugin.json"])["version"])
        self.assertEqual("0.1.1-dev", json.loads(changed[self.prefix + "references/SOURCE_MAP.json"])["adapter_version"])
        self.assertEqual(set(self.files), set(changed))

    def test_bad_versions_rejected(self):
        for value in ("v1.0.0", "1.0.0-rc.x", "../secret", "", "1.0.0; echo hello"):
            with self.subTest(value=value), self.assertRaises(common.BuildError):
                plugin.build_files(value)

    def test_missing_canonical_reference_fails(self):
        original = common.read_source
        def unavailable(path):
            if path == "knowledge/07_Quality_Assurance.md":
                raise common.BuildError("Missing canonical source")
            return original(path)
        with patch.object(common, "read_source", side_effect=unavailable):
            with self.assertRaisesRegex(common.BuildError, "Missing canonical"):
                plugin.build_files()

    def test_reference_map_tamper_fails(self):
        original = common.read_source
        def drift(path):
            content = original(path)
            if path == "platforms/shared/REFERENCE_MAP.json":
                obj = json.loads(content)
                obj["files"].pop()
                return json.dumps(obj).encode("utf-8")
            return content
        with patch.object(common, "read_source", side_effect=drift):
            with self.assertRaisesRegex(common.BuildError, "drift"):
                plugin.build_files()

    def test_runtime_manifest_module_tamper_fails(self):
        original = common.read_source
        def drift(path):
            content = original(path)
            if path == "package/01_MANIFEST.json":
                obj = json.loads(content)
                obj["modules"]["supporting"].pop()
                return json.dumps(obj).encode("utf-8")
            return content
        with patch.object(common, "read_source", side_effect=drift):
            with self.assertRaisesRegex(common.BuildError, r"11\+11"):
                plugin.build_files()

    def test_plugin_manifest_mcp_injection_rejected(self):
        original = plugin.read_source
        def injected(path):
            content = original(path)
            if path == "platforms/chatgpt/plugin.json":
                obj = json.loads(content)
                obj["mcpServers"] = "./mcp.json"
                return json.dumps(obj).encode("utf-8")
            return content
        with patch.object(plugin, "read_source", side_effect=injected):
            with self.assertRaisesRegex(common.BuildError, "Unexpected root fields"):
                plugin.build_files()

    def test_plugin_manifest_unsafe_extension_rejected(self):
        original = plugin.read_source
        def injected(path):
            content = original(path)
            if path == "platforms/chatgpt/plugin.json":
                obj = json.loads(content)
                obj["extensions"]["com.openai"]["hooks"] = "./hooks/hooks.json"
                return json.dumps(obj).encode("utf-8")
            return content
        with patch.object(plugin, "read_source", side_effect=injected):
            with self.assertRaisesRegex(common.BuildError, "Only OpenAI presentation metadata"):
                plugin.build_files()

    def test_plugin_schema_and_name_changes_rejected(self):
        for key, value in (("$schema", "https://example.org/schema.json"), ("name", "other-plugin")):
            original = plugin.read_source
            def modified(path):
                data = original(path)
                if path == "platforms/chatgpt/plugin.json":
                    obj = json.loads(data)
                    obj[key] = value
                    return json.dumps(obj).encode("utf-8")
                return data
            with self.subTest(key=key), patch.object(plugin, "read_source", side_effect=modified):
                with self.assertRaisesRegex(common.BuildError, "schema or stable plugin identifier"):
                    plugin.build_files()

    def test_invalid_relative_link_rejected(self):
        modified = dict(self.files)
        skill = self.prefix + "SKILL.md"
        modified[skill] = modified[skill].replace(b"references/OUTPUT_CONTRACT.md", b"references/NOT_A_FILE.md")
        with self.assertRaisesRegex(common.BuildError, "Broken skill link"):
            plugin.validate_plugin_files(modified)

    def test_unapproved_and_traversal_paths_rejected(self):
        modified = dict(self.files)
        victim = self.prefix + "references/BUILDER_INDEX.md"
        body = modified.pop(victim)
        modified["private/BUILDER_INDEX.md"] = body
        with self.assertRaisesRegex(common.BuildError, "Unauthorized"):
            plugin.validate_plugin_files(modified)
        modified.pop("private/BUILDER_INDEX.md")
        modified["skills/aio-ai-builder/references/../.env"] = body
        with self.assertRaises(common.BuildError):
            plugin.validate_plugin_files(modified)


if __name__ == "__main__":
    unittest.main()
