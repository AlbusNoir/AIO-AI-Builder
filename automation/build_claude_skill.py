#!/usr/bin/env python3
"""Build a reproducible Claude Skills ZIP from approved AIO Builder sources.

This is a Phase 2 reference implementation. No network, API keys, or host tools.
It intentionally does not modify the canonical runtime package or release tags.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

REPO = Path(__file__).resolve().parents[1]
SKILL_NAME = "aio-ai-builder"
FIXED_TIMESTAMP = (2020, 1, 1, 0, 0, 0)
DEFAULT_VERSION = "0.1.3-dev"
ALLOWED_BUILDER_FILES = {
    f"knowledge/{name}" for name in (
        "00_Master_Index.md", "01_Design_Principles.md", "02_Instruction_Building_Blocks.md",
        "03_Domain_Templates.md", "04_Response_Patterns.md", "05_Persona_Library.md",
        "06_Tool_Capability_Patterns.md", "07_Quality_Assurance.md", "08_Assistant_Examples.md",
    )
}
ALLOWED_RUNTIME_BASICS = {
    "package/PASTE_THIS_INTO_THE_GPT.txt", "package/01_MANIFEST.json",
    "package/02_MASTER_OPERATING_SPEC.md",
}
ALLOWED_CONTRACTS = {
    f"package/references/canonical/{name}" for name in (
        "REF-CN-001_Canonical_Module_Contract.md",
        "REF-CN-002_Canonical_Capability_Contract.md",
        "REF-CN-003_Canonical_Identifier_Registry.md",
        "REF-CN-004_Canonical_Package_Manifest_Schema.md",
    )
}


class BuildError(RuntimeError):
    pass


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_relpath(raw: str) -> PurePosixPath:
    path = PurePosixPath(raw)
    if not raw or path.is_absolute() or any(seg in ("", ".", "..") for seg in raw.split("/")):
        raise BuildError(f"Unsafe or noncanonical relative path: {raw!r}")
    if "\\" in raw or ":" in raw or any(seg.startswith(".") for seg in path.parts):
        raise BuildError(f"Disallowed relative path: {raw!r}")
    return path


def read_source(relative: str) -> bytes:
    path = REPO.joinpath(*safe_relpath(relative).parts)
    if not path.is_file() or path.is_symlink() or not path.resolve().is_relative_to(REPO.resolve()):
        raise BuildError(f"Required canonical source missing, symlinked or outside repository: {relative}")
    return path.read_bytes()


def check_skill_frontmatter(content: str) -> None:
    m = re.match(r"\A---\n(.*?)\n---\n", content, flags=re.S)
    if not m:
        raise BuildError("Claude SKILL.md missing YAML frontmatter")
    fields = {}
    for line in m.group(1).splitlines():
        k, sep, v = line.partition(":")
        if not sep or k.strip() in fields or k.strip() not in ("name", "description"):
            raise BuildError("Skill frontmatter must use unique name/description fields only")
        fields[k.strip()] = v.strip().strip('"\'')
    if fields.get("name") != SKILL_NAME:
        raise BuildError("Skill name must match named ZIP folder")
    if not (10 <= len(fields.get("description", "")) <= 200):
        raise BuildError("Skill description length must be 10-200 characters")


def source_commit() -> str | None:
    if not (REPO / ".git").exists():
        return None
    dirty = subprocess.run(["git", "-C", str(REPO), "status", "--porcelain", "--untracked-files=normal"],
                           capture_output=True, text=True, check=False)
    if dirty.returncode != 0 or dirty.stdout.strip():
        # HEAD cannot be asserted as the exact source of an uncommitted build.
        return None
    p = subprocess.run(["git", "-C", str(REPO), "rev-parse", "--verify", "HEAD"],
                       capture_output=True, text=True, check=False)
    value = p.stdout.strip()
    return value if p.returncode == 0 and re.fullmatch(r"[0-9a-f]{40,64}", value) else None


def validate_inventory(entries: list[dict]) -> None:
    manifest = json.loads(read_source("package/01_MANIFEST.json"))
    module_source_paths = {
        "package/" + module["path"]
        for family in ("governing", "supporting")
        for module in manifest["modules"][family]
    }
    module_entry_paths = {entry["source"] for entry in entries if entry["role"] == "target-runtime-module-reference"}
    if module_source_paths != module_entry_paths:
        raise BuildError(f"Runtime module allowlist differs from canonical manifest: missing={sorted(module_source_paths-module_entry_paths)}, extra={sorted(module_entry_paths-module_source_paths)}")
    if len(manifest["modules"]["governing"]) != 11 or len(manifest["modules"]["supporting"]) != 11:
        raise BuildError("Unexpected canonical 11 governing / 11 supporting inventory")
    expected_sources = ALLOWED_BUILDER_FILES | ALLOWED_RUNTIME_BASICS | ALLOWED_CONTRACTS | module_source_paths
    given_sources = {e["source"] for e in entries}
    if expected_sources != given_sources:
        raise BuildError(f"Reference allowlist differs from approved inputs: missing={sorted(expected_sources-given_sources)}, extra={sorted(given_sources-expected_sources)}")
    for entry in entries:
        source = entry["source"]
        if source in ALLOWED_BUILDER_FILES:
            role, destination = "builder-design-reference", "references/builder/" + source.removeprefix("knowledge/")
        elif source in ALLOWED_RUNTIME_BASICS:
            role, destination = "target-runtime-reference", "references/runtime/" + source.removeprefix("package/")
        elif source in ALLOWED_CONTRACTS:
            role, destination = "target-runtime-contract-reference", "references/runtime/" + source.removeprefix("package/")
        else:
            role, destination = "target-runtime-module-reference", "references/runtime/" + source.removeprefix("package/")
        if entry["role"] != role or entry["target"] != destination:
            raise BuildError(f"Unexpected source role/path mapping for {source}")


def builder_index(entries: list[dict]) -> str:
    lines = [
        "# AIO AI Builder - Bundled Reference Index", "",
        "This is a navigation file generated from the approved source allowlist. Files under `builder/` are **Builder design references**. Files under `runtime/` are **templates for the assistant being designed**, not Builder operating instructions.",
        "", "## Recommended Builder references (load selectively)", "",
        "| Purpose | Source |", "|---|---|",
    ]
    for entry in entries:
        if entry["role"] == "builder-design-reference":
            base = Path(entry["source"]).stem
            lines.append(f"| {base.replace('_', ' ')} | [{base}](builder/{Path(entry['target']).name}) |")
    lines += [
        "", "Use design principles, building blocks, templates, response patterns, personas, capability patterns, QA or examples when relevant. The original master index guides selection; examples are not mandates.",
        "", "## Target assistant runtime references (design-time only)", "",
        "Start with [Runtime Master Operating Spec](runtime/02_MASTER_OPERATING_SPEC.md), [Runtime Manifest](runtime/01_MANIFEST.json), and [Target Bootstrap](runtime/PASTE_THIS_INTO_THE_GPT.txt) **only when constructing or reviewing the generated assistant's runtime architecture**.",
        "", "### Canonical contracts", "",
    ]
    for entry in entries:
        if entry["role"] == "target-runtime-contract-reference":
            target = entry["target"].removeprefix("references/")
            lines.append(f"- [{Path(target).stem}](<{target}>)")
    lines += ["", "### Governing modules", ""]
    for entry in entries:
        if entry["role"] == "target-runtime-module-reference" and "/governing/" in entry["target"]:
            target = entry["target"].removeprefix("references/")
            lines.append(f"- [{Path(target).stem}](<{target}>)")
    lines += ["", "### Supporting modules", ""]
    for entry in entries:
        if entry["role"] == "target-runtime-module-reference" and "/supporting/" in entry["target"]:
            target = entry["target"].removeprefix("references/")
            lines.append(f"- [{Path(target).stem}](<{target}>)")
    lines += [
        "", "Read only modules whose behavior materially contributes to the target assistant. Preserve canonical ownership, activation conditions and capability honesty. The original runtime manifest carries its existing internal version/status unchanged; it is **not** the Claude skill version.",
        "", "## Source copy verification", "",
        "`SOURCE_MAP.json` lists SHA-256 hashes for the exact canonical source bytes in this skill. Source copies are not paraphrases or synthesized replacements.", "",
    ]
    return "\n".join(lines)


def build_files(version: str = DEFAULT_VERSION) -> dict[str, bytes]:
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+(?:(?:-dev(?:\.[0-9]+)?)|(?:-rc\.[0-9]+))?", version):
        raise BuildError("Use an adapter version such as 0.1.0-dev, 1.1.0-rc.1 or 1.1.0")
    spec = json.loads(read_source("platforms/shared/REFERENCE_MAP.json"))
    if spec.get("format_version") != 1 or spec.get("bundle") != "claude-builder-reference":
        raise BuildError("Unexpected allowlist schema")
    entries = spec["files"]
    if not isinstance(entries, list) or not entries:
        raise BuildError("Empty reference allowlist")
    validate_inventory(entries)
    files: dict[str, bytes] = {}
    tracked = []
    seen_sources, seen_targets = set(), set()
    for entry in entries:
        if set(entry) != {"source", "target", "role"}:
            raise BuildError("Unexpected reference map entry fields")
        source, target = entry["source"], entry["target"]
        safe_relpath(source)
        safe_relpath(target)
        if not target.startswith("references/"):
            raise BuildError(f"Reference outside skill references/: {target}")
        if source in seen_sources or target.casefold() in seen_targets:
            raise BuildError(f"Duplicate or case-colliding source/target: {source} -> {target}")
        seen_sources.add(source)
        seen_targets.add(target.casefold())
        content = read_source(source)
        files[target] = content
        tracked.append({"source": source, "bundled": target, "role": entry["role"], "sha256": sha256(content)})
    files["SKILL.md"] = read_source("platforms/claude/SKILL.md")
    check_skill_frontmatter(files["SKILL.md"].decode("utf-8"))
    for name in ("BUILDER_CONTRACT.md", "OUTPUT_CONTRACT.md"):
        files[f"references/{name}"] = read_source(f"platforms/shared/{name}")
    files["references/BUILDER_INDEX.md"] = builder_index(entries).encode("utf-8")
    origin = source_commit()
    metadata = {
        "adapter": "claude",
        "skill": SKILL_NAME,
        "adapter_version": version,
        "source_commit": origin,
        "source_commit_verification": "clean-git-HEAD" if origin else "unavailable-from-snapshot-or-dirty-worktree",
        "runtime_material_use": "reference-only-for-generated-assistants",
        "source_files": tracked,
    }
    files["references/SOURCE_MAP.json"] = (json.dumps(metadata, indent=2, sort_keys=True) + "\n").encode("utf-8")
    return files


def validate_paths(files: dict[str, bytes]) -> None:
    # Only generated top-level and relative Markdown paths, not arbitrary filesystem references.
    if not files["SKILL.md"].startswith(b"---\n"):
        raise BuildError("Missing skill frontmatter")
    for rel in ("SKILL.md", "references/BUILDER_INDEX.md"):
        text = files[rel].decode("utf-8")
        for destination in re.findall(r"\]\(<?([^)>]+)>?\)", text):
            if "://" in destination or destination.startswith("#"):
                continue
            src_parent = PurePosixPath(rel).parent
            try:
                joined = (src_parent / destination).as_posix()
                safe_relpath(joined)
            except BuildError as e:
                raise BuildError(f"Invalid link {destination!r} in {rel}: {e}") from e
            if joined not in files:
                raise BuildError(f"Broken bundled link {destination!r} in {rel}")
    if set(files) != set(map(str, files)) or any(not k.startswith("references/") and k != "SKILL.md" for k in files):
        raise BuildError("Unexpected output outside skill allowlist")


def make_zip(output: Path, files: dict[str, bytes]) -> str:
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "w", compression=ZIP_DEFLATED, compresslevel=9, strict_timestamps=True) as z:
        for relative, content in sorted(files.items()):
            p = safe_relpath(relative)
            info = ZipInfo(f"{SKILL_NAME}/{p.as_posix()}", FIXED_TIMESTAMP)
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            z.writestr(info, content, compress_type=ZIP_DEFLATED, compresslevel=9)
    digest = sha256(output.read_bytes())
    (output.parent / (output.name + ".sha256")).write_text(f"{digest}  {output.name}\n", encoding="utf-8")
    return digest


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output-dir", type=Path, default=REPO / "dist")
    ap.add_argument("--adapter-version", default=DEFAULT_VERSION)
    args = ap.parse_args()
    try:
        files = build_files(args.adapter_version)
        validate_paths(files)
        zip_file = args.output_dir / f"AIO-AI-Builder-Claude-Skill-{args.adapter_version}.zip"
        digest = make_zip(zip_file, files)
    except (BuildError, KeyError, ValueError, OSError) as error:
        print(f"CLAUDE SKILL BUILD FAILED: {error}", file=sys.stderr)
        return 1
    print(f"Built {zip_file} ({len(files)} files; SHA-256 {digest})")
    print("Local structural build only: Claude installation/activation remains unverified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
