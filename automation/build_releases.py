#!/usr/bin/env python3
"""Stage and verify all four AIO AI Builder platform release artifacts.

Uses the existing tested platform builders; does not publish, create tags,
modify package/, or grant host capabilities. The canonical package-only release
remains owned by the existing Gitea release workflow.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from zipfile import ZipFile

import build_chatgpt_plugin as chatgpt
import build_claude_skill as claude
import build_gemini_skill as gemini
import platform_skill_common as common

REPO = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = REPO / "dist" / "release-stage"
MARKER = "build-manifest.json"
VERSION_MAP = {
    "chatgpt": chatgpt.DEFAULT_VERSION,
    "claude": claude.DEFAULT_VERSION,
    "gemini": gemini.DEFAULT_VERSION,
}


class ReleaseBuildError(RuntimeError):
    """The staged release failed its deterministic safety checks."""


def run_checks() -> None:
    """Run self-contained public suites; the private model regression corpus is excluded."""
    commands = [
        [sys.executable, "-B", "run_tests.py"],
        [sys.executable, "-B", "tests/08_package_contract/package_contract.py"],
        [sys.executable, "-B", "tests/09_v2_behavioral/run_static_contract.py"],
    ]
    for command in commands:
        print(f"Running: {' '.join(command)}", flush=True)
        subprocess.run(command, cwd=REPO, check=True)


def expected_outputs(versions: dict[str, str]) -> dict[str, dict[str, bytes]]:
    """Independently compute the exact allowlisted bytes expected in each archive."""
    c = chatgpt.build_files(versions["chatgpt"])
    cl = claude.build_files(versions["claude"])
    g = gemini.build_files(versions["gemini"])
    c_sources = json.loads(c[chatgpt.SKILL_DIR + "references/SOURCE_MAP.json"])
    cl_sources = json.loads(cl["references/SOURCE_MAP.json"])
    g_sources = json.loads(g["references/SOURCE_MAP.json"])
    for doc in (cl_sources, g_sources):
        if [(s["source"], s["sha256"]) for s in doc["source_files"]] != [
            (s["source"], s["sha256"]) for s in c_sources["source_files"]
        ]:
            raise ReleaseBuildError("Cross-platform canonical source provenance mismatch")
    return {
        f"AIO-AI-Builder-ChatGPT-Plugin-{versions['chatgpt']}.zip": c,
        f"AIO-AI-Builder-Claude-Skill-{versions['claude']}.zip": {
            f"{common.SKILL_NAME}/{name}": data for name, data in cl.items()
        },
        f"AIO-AI-Builder-Gemini-Apps-Skill-{versions['gemini']}.zip": g,
        f"AIO-AI-Builder-Gemini-CLI-Skill-{versions['gemini']}.skill": {
            f"{common.SKILL_NAME}/{name}": data for name, data in g.items()
        },
    }


def verify_archive(archive: Path, expected: dict[str, bytes]) -> dict:
    """Verify archive structure, every payload byte, and the matching checksum."""
    if not archive.is_file() or archive.is_symlink():
        raise ReleaseBuildError(f"Missing/nonregular artifact: {archive.name}")
    with ZipFile(archive) as bundle:
        infos = bundle.infolist()
        names = [info.filename for info in infos]
        if len(names) != len(expected) or set(names) != set(expected):
            raise ReleaseBuildError(f"Unexpected or missing ZIP entries in {archive.name}")
        if len(set(n.casefold() for n in names)) != len(names):
            raise ReleaseBuildError(f"Duplicate/colliding ZIP paths in {archive.name}")
        if bundle.testzip() is not None:
            raise ReleaseBuildError(f"Corrupt ZIP member in {archive.name}")
        for info in infos:
            common.safe_relative(info.filename)
            if info.is_dir() or info.flag_bits & 1:
                raise ReleaseBuildError(f"Unexpected directory/encrypted member in {archive.name}")
            # Archive content must be regular files, never symlinks or scripts.
            if (info.external_attr >> 16) & 0o170000 != 0o100000:
                raise ReleaseBuildError(f"Nonregular ZIP entry: {info.filename}")
            if bundle.read(info.filename) != expected[info.filename]:
                raise ReleaseBuildError(f"Content/provenance mismatch: {info.filename}")
    digest = common.sha256(archive.read_bytes())
    checksum_path = archive.with_name(archive.name + ".sha256")
    if not checksum_path.is_file() or checksum_path.read_text(encoding="utf-8") != f"{digest}  {archive.name}\n":
        raise ReleaseBuildError(f"Checksum mismatch: {archive.name}")
    return {"name": archive.name, "sha256": digest, "bytes": archive.stat().st_size, "files": len(expected)}


def build_once(dest: Path, versions: dict[str, str]) -> list[dict]:
    """Generate using the already accepted builders; validate against their allowlists."""
    expectations = expected_outputs(versions)
    chatgpt.build_artifact(dest, versions["chatgpt"])
    claude_files = claude.build_files(versions["claude"])
    claude.validate_paths(claude_files)
    claude.make_zip(dest / f"AIO-AI-Builder-Claude-Skill-{versions['claude']}.zip", claude_files)
    gemini.build_artifacts(dest, versions["gemini"])
    reports = [verify_archive(dest / name, expected) for name, expected in sorted(expectations.items())]
    allowed = {record["name"] for record in reports}
    allowed |= {name + ".sha256" for name in allowed}
    extra = {p.name for p in dest.iterdir()} - allowed
    if extra:
        raise ReleaseBuildError(f"Unexpected output in release staging: {sorted(extra)}")
    return reports


def write_reports(dest: Path, versions: dict[str, str], archives: list[dict], tests: bool) -> None:
    manifest = {
        "format_version": 1,
        "product": "AIO AI Builder - platform adapters",
        "scope": "staged artifacts only; not published or installed",
        "adapter_versions": versions,
        "source_commit": common.source_commit(),
        "tests": "deterministic suites passed" if tests else "not run (--skip-tests)",
        "archives": archives,
    }
    (dest / MARKER).write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (dest / "SHA256SUMS.txt").write_text(
        "".join(f"{record['sha256']}  {record['name']}\n" for record in archives), encoding="utf-8"
    )
    lines = [
        "# AIO AI Builder - staged platform release", "",
        "Status: **STRUCTURE VERIFIED**. These artifacts have not been installed, activated, or published by this runner.",
        "", f"Deterministic tests: {manifest['tests']}.",
        f"Source commit: `{manifest['source_commit'] or 'not verifiable from this workspace'}`.",
        "", "| Platform artifact | SHA-256 | Files |", "|---|---|---:|",
    ]
    lines += [f"| `{r['name']}` | `{r['sha256']}` | {r['files']} |" for r in archives]
    lines += [
        "", "The canonical `package/`-only archive is **not generated here**. The existing Gitea release workflow owns that separate artifact.",
        "", "A common `--adapter-version` is optional. Without it, each adapter keeps its independently tested default version.",
        "", "Verify installation and behavior on each host separately before claiming plug-and-play acceptance.", "",
    ]
    (dest / "build-report.md").write_text("\n".join(lines), encoding="utf-8")


def output_guard(target: Path, replace: bool) -> None:
    if target.is_symlink():
        raise ReleaseBuildError("Refusing symlink output directory")
    if target.exists():
        if not target.is_dir():
            raise ReleaseBuildError("Output is not a directory")
        if any(target.iterdir()):
            if not replace:
                raise ReleaseBuildError("Output already contains files; use --replace for a previous runner-owned stage")
            marker = target / MARKER
            if not marker.is_file() or marker.is_symlink():
                raise ReleaseBuildError("Cannot replace output without the runner's build-manifest.json")
            try:
                obj = json.loads(marker.read_text(encoding="utf-8"))
            except (ValueError, UnicodeError) as error:
                raise ReleaseBuildError("Existing output has invalid build manifest") from error
            if obj.get("format_version") != 1 or obj.get("product") != "AIO AI Builder - platform adapters":
                raise ReleaseBuildError("Existing output is not owned by this runner")
            allowed = {MARKER, "SHA256SUMS.txt", "build-report.md"}
            allowed.update(item["name"] for item in obj.get("archives", []))
            allowed.update(item["name"] + ".sha256" for item in obj.get("archives", []))
            if {p.name for p in target.iterdir()} != allowed or any(p.is_symlink() or not p.is_file() for p in target.iterdir()):
                raise ReleaseBuildError("Existing output contains unexpected or unsafe files; refusing replacement")


def stage_release(output_dir: Path, versions: dict[str, str], *, run_tests: bool = True,
                  replace: bool = False) -> Path:
    output = output_dir.absolute()
    # Never overwrite an input tree or the repository itself.
    prohibited = {REPO.resolve(), (REPO / "package").resolve(), (REPO / "platforms").resolve(), (REPO / "automation").resolve()}
    if output.resolve() in prohibited or any(output.resolve().is_relative_to(p) for p in prohibited - {REPO.resolve()}):
        raise ReleaseBuildError("Output must not be an input/source directory")
    output_guard(output, replace)
    if run_tests:
        run_checks()
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="aio_release_build_", dir=output.parent) as first_tmp, \
         tempfile.TemporaryDirectory(prefix="aio_release_compare_") as second_tmp:
        first, second = Path(first_tmp), Path(second_tmp)
        records = build_once(first, versions)
        other = build_once(second, versions)
        if [(r["name"], r["sha256"]) for r in records] != [(r["name"], r["sha256"]) for r in other]:
            raise ReleaseBuildError("Reproducibility failure: repeated builds differ")
        write_reports(first, versions, records, run_tests)
        if output.exists() and any(output.iterdir()):
            # The old stage is preserved until the new build has fully passed.
            backup = output.parent / (output.name + ".previous")
            if backup.exists():
                raise ReleaseBuildError("Refusing to overwrite existing .previous directory")
            output.rename(backup)
            try:
                first.rename(output)
            except BaseException:
                backup.rename(output)
                raise
            shutil.rmtree(backup)
        else:
            if output.exists():
                output.rmdir()
            first.rename(output)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--all", action="store_true", help="Build all four adapters (default behavior)")
    parser.add_argument("--adapter-version", help="Override all adapter versions with one reviewed version (e.g. 1.1.0)")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--skip-tests", action="store_true", help="Only for development; mark tests as not run")
    parser.add_argument("--replace", action="store_true", help="Replace only a previous runner-owned stage")
    args = parser.parse_args()
    versions = {kind: args.adapter_version or default for kind, default in VERSION_MAP.items()}
    try:
        result = stage_release(args.output_dir, versions, run_tests=not args.skip_tests, replace=args.replace)
    except (ReleaseBuildError, common.BuildError, claude.BuildError, ValueError, OSError,
            subprocess.CalledProcessError, UnicodeError) as error:
        print(f"Release staging FAILED: {error}", file=sys.stderr)
        return 1
    print(f"\nSTRUCTURE VERIFIED - four platform artifacts staged in {result}")
    print("See build-manifest.json, build-report.md, and SHA256SUMS.txt.")
    print("No tag, release, publication, installation, or live behavioral test was performed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
