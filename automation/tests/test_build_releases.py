"""Unified release runner invariants (no host or release publication required)."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile, ZipInfo

AUTOMATION = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AUTOMATION))
import build_releases as release  # noqa: E402


class UnifiedReleaseRunnerTests(unittest.TestCase):
    def setUp(self):
        self.work = tempfile.TemporaryDirectory()
        self.addCleanup(self.work.cleanup)
        self.root = Path(self.work.name)

    def test_four_platforms_layouts_and_reproducibility(self):
        first = release.stage_release(self.root / "first", release.VERSION_MAP, run_tests=False)
        second = release.stage_release(self.root / "second", release.VERSION_MAP, run_tests=False)
        a = json.loads((first / "build-manifest.json").read_text(encoding="utf-8"))
        b = json.loads((second / "build-manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(a, b)
        self.assertEqual(4, len(a["archives"]))
        self.assertEqual("not run (--skip-tests)", a["tests"])
        for x in a["archives"]:
            self.assertEqual((first / x["name"]).read_bytes(), (second / x["name"]).read_bytes())
            with ZipFile(first / x["name"]) as z:
                self.assertIsNone(z.testzip())
                if "ChatGPT" in x["name"]:
                    self.assertIn("plugin.json", z.namelist())
                    self.assertIn("skills/aio-ai-builder/SKILL.md", z.namelist())
                elif "Gemini-Apps" in x["name"]:
                    self.assertIn("SKILL.md", z.namelist())
                else:
                    self.assertIn("aio-ai-builder/SKILL.md", z.namelist())
        self.assertEqual(4, len((first / "SHA256SUMS.txt").read_text().splitlines()))

    def test_existing_unowned_files_never_deleted(self):
        folder = self.root / "existing"
        folder.mkdir()
        (folder / "precious.txt").write_text("preserve", encoding="utf-8")
        for replace in (False, True):
            with self.subTest(replace=replace), self.assertRaises(release.ReleaseBuildError):
                release.stage_release(folder, release.VERSION_MAP, run_tests=False, replace=replace)
        self.assertEqual("preserve", (folder / "precious.txt").read_text())

    def test_replace_only_owned_output(self):
        folder = self.root / "release"
        release.stage_release(folder, release.VERSION_MAP, run_tests=False)
        with self.assertRaises(release.ReleaseBuildError):
            release.stage_release(folder, release.VERSION_MAP, run_tests=False)
        release.stage_release(folder, release.VERSION_MAP, run_tests=False, replace=True)
        self.assertTrue((folder / "build-report.md").is_file())
        self.assertFalse((self.root / "release.previous").exists())

    def test_tampered_manifest_refuses_replace(self):
        folder = self.root / "release"
        release.stage_release(folder, release.VERSION_MAP, run_tests=False)
        (folder / "unexpected-file").write_text("do not erase", encoding="utf-8")
        with self.assertRaises(release.ReleaseBuildError):
            release.stage_release(folder, release.VERSION_MAP, run_tests=False, replace=True)
        self.assertTrue((folder / "unexpected-file").exists())

    def test_tampered_zip_byte_fails_validation(self):
        stage = self.root / "stage"
        stage.mkdir()
        expected = release.expected_outputs(release.VERSION_MAP)
        path, files = next(iter(expected.items()))
        out = stage / path
        with ZipFile(out, "w") as z:
            for name, data in files.items():
                z.writestr(name, data + b"bad" if name.endswith("SKILL.md") else data)
        out.with_name(out.name + ".sha256").write_text(
            f"{release.common.sha256(out.read_bytes())}  {out.name}\n"
        )
        with self.assertRaises(release.ReleaseBuildError):
            release.verify_archive(out, files)

    def test_version_override_is_consistent(self):
        versions = dict.fromkeys(release.VERSION_MAP, "1.1.0")
        out = release.stage_release(self.root / "uniform", versions, run_tests=False)
        manifest = json.loads((out / "build-manifest.json").read_text())
        self.assertEqual(set(manifest["adapter_versions"].values()), {"1.1.0"})
        self.assertTrue(all("1.1.0" in x["name"] for x in manifest["archives"]))


if __name__ == "__main__":
    unittest.main()
