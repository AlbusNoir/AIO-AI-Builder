"""Canonical-source bundling utilities for AIO AI Builder platform skills.

The builder and runtime references are copied byte-for-byte. Generated navigation
metadata is not a new normative specification. No network or runtime action code.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path, PurePosixPath
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

REPO = Path(__file__).resolve().parents[1]
SKILL_NAME = "aio-ai-builder"
FIXED_TIMESTAMP = (2020, 1, 1, 0, 0, 0)
BUILDER_FILES = {f"knowledge/{name}" for name in (
    "00_Master_Index.md", "01_Design_Principles.md", "02_Instruction_Building_Blocks.md",
    "03_Domain_Templates.md", "04_Response_Patterns.md", "05_Persona_Library.md",
    "06_Tool_Capability_Patterns.md", "07_Quality_Assurance.md", "08_Assistant_Examples.md",
)}
RUNTIME_BASICS = {
    "package/PASTE_THIS_INTO_THE_GPT.txt", "package/01_MANIFEST.json",
    "package/02_MASTER_OPERATING_SPEC.md",
}
CONTRACTS = {f"package/references/canonical/{name}" for name in (
    "REF-CN-001_Canonical_Module_Contract.md",
    "REF-CN-002_Canonical_Capability_Contract.md",
    "REF-CN-003_Canonical_Identifier_Registry.md",
    "REF-CN-004_Canonical_Package_Manifest_Schema.md",
)}


class BuildError(RuntimeError):
    """A bundle cannot be built safely from the available canonical inputs."""


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_relative(path: str) -> PurePosixPath:
    p = PurePosixPath(path)
    if (not path or not isinstance(path, str) or p.is_absolute() or
            any(s in ("", ".", "..") or s.startswith(".") for s in path.split("/")) or
            "\\" in path or ":" in path or "\x00" in path):
        raise BuildError(f"Unsafe or noncanonical relative path: {path!r}")
    return p


def read_source(relative: str) -> bytes:
    file = REPO.joinpath(*safe_relative(relative).parts)
    if not file.is_file() or file.is_symlink() or not file.resolve().is_relative_to(REPO.resolve()):
        raise BuildError(f"Missing, symlinked or out-of-repository source: {relative}")
    return file.read_bytes()


def source_commit() -> str | None:
    """Only record a commit if the complete checkout is clean."""
    if not (REPO / ".git").exists():
        return None
    status = subprocess.run(["git", "-C", str(REPO), "status", "--porcelain", "--untracked-files=normal"],
                            capture_output=True, text=True, check=False)
    if status.returncode or status.stdout.strip():
        return None
    commit = subprocess.run(["git", "-C", str(REPO), "rev-parse", "--verify", "HEAD"],
                            capture_output=True, text=True, check=False)
    sha = commit.stdout.strip()
    return sha if not commit.returncode and re.fullmatch(r"[0-9a-f]{40,64}", sha) else None


def check_frontmatter(text: str) -> None:
    # Validate that the SKILL.md file has the correct YAML frontmatter. Don't error on CRLF
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", text, re.S)
    if not match:
        raise BuildError("SKILL.md requires YAML frontmatter as its first content")
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        key, sep, value = line.partition(":")
        key = key.strip()
        if not sep or key not in ("name", "description") or key in fields:
            raise BuildError("SKILL.md frontmatter must contain unique name and description only")
        fields[key] = value.strip().strip('"\'')
    if fields.get("name") != SKILL_NAME:
        raise BuildError("SKILL.md name must be aio-ai-builder")
    if not 10 <= len(fields.get("description", "")) <= 200:
        raise BuildError("SKILL.md description must be between 10 and 200 characters")


def allowed_entries() -> list[dict]:
    """Validate the shared reference map against the actual runtime manifest."""
    try:
        spec = json.loads(read_source("platforms/shared/REFERENCE_MAP.json"))
        manifest = json.loads(read_source("package/01_MANIFEST.json"))
    except (ValueError, KeyError) as error:
        raise BuildError(f"Invalid canonical inventory JSON: {error}") from error
    # Name kept for backward compatibility with the previously accepted Claude
    # source map; the contents and path targets are shared across platforms.
    if spec.get("format_version") != 1 or spec.get("bundle") != "claude-builder-reference":
        raise BuildError("Unexpected shared reference-map version/identifier")
    entries = spec.get("files")
    if not isinstance(entries, list) or not entries:
        raise BuildError("Empty or invalid reference map")
    try:
        governing = manifest["modules"]["governing"]
        supporting = manifest["modules"]["supporting"]
        module_paths = {"package/" + x["path"] for x in governing + supporting}
    except (KeyError, TypeError) as error:
        raise BuildError(f"Malformed canonical module manifest: {error}") from error
    if len(governing) != 11 or len(supporting) != 11 or len(module_paths) != 22:
        raise BuildError("Canonical runtime manifest must have 11+11 unique modules")
    expected = BUILDER_FILES | RUNTIME_BASICS | CONTRACTS | module_paths
    actual = {x.get("source") for x in entries if isinstance(x, dict)}
    if actual != expected or len(entries) != len(expected):
        raise BuildError(f"Shared reference map drift: missing {sorted(expected-actual)}, extra {sorted(actual-expected)}")
    seen_targets: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict) or set(entry) != {"source", "target", "role"}:
            raise BuildError("Unexpected entry fields in reference map")
        source, target = entry["source"], entry["target"]
        safe_relative(source)
        safe_relative(target)
        if source in BUILDER_FILES:
            role, destination = "builder-design-reference", "references/builder/" + source.removeprefix("knowledge/")
        elif source in RUNTIME_BASICS:
            role, destination = "target-runtime-reference", "references/runtime/" + source.removeprefix("package/")
        elif source in CONTRACTS:
            role, destination = "target-runtime-contract-reference", "references/runtime/" + source.removeprefix("package/")
        else:
            role, destination = "target-runtime-module-reference", "references/runtime/" + source.removeprefix("package/")
        if entry["role"] != role or entry["target"] != destination:
            raise BuildError(f"Wrong source role/destination for {source}")
        if target.casefold() in seen_targets:
            raise BuildError(f"Duplicate or case-colliding destination {target}")
        seen_targets.add(target.casefold())
    module_entries = {x["source"] for x in entries if x["role"] == "target-runtime-module-reference"}
    if module_entries != module_paths:
        raise BuildError("Module references differ from the canonical manifest")
    return entries


def reference_index(entries: list[dict], platform: str) -> bytes:
    lines = [
        "# AIO AI Builder - Bundled Reference Index", "",
        "Use files under `builder/` as Builder design references. Files under `runtime/` are **templates for the assistant being designed**, never automatic instructions governing this Builder skill.",
        "", "## Builder design reference library", "", "| Purpose | Source |", "|---|---|",
    ]
    for entry in entries:
        if entry["role"] == "builder-design-reference":
            name = Path(entry["source"]).stem
            lines.append(f"| {name.replace('_', ' ')} | [{name}](builder/{Path(entry['target']).name}) |")
    lines.extend([
        "", "Read only the design sources needed for this task. The original Builder master index describes the library; examples are not requirements.",
        "", "## Generated-assistant runtime references (design use only)", "",
        "Consult [Runtime Master Spec](runtime/02_MASTER_OPERATING_SPEC.md), [Runtime Manifest](runtime/01_MANIFEST.json), and [Target Bootstrap](runtime/PASTE_THIS_INTO_THE_GPT.txt) only when constructing or auditing the target assistant's runtime configuration.",
        "", "### Canonical contracts", "",
    ])
    for entry in entries:
        if entry["role"] == "target-runtime-contract-reference":
            target = entry["target"].removeprefix("references/")
            lines.append(f"- [{Path(target).stem}](<{target}>)")
    for kind in ("governing", "supporting"):
        lines.extend(["", f"### {kind.capitalize()} modules", ""])
        for entry in entries:
            if entry["role"] == "target-runtime-module-reference" and f"/{kind}/" in entry["target"]:
                target = entry["target"].removeprefix("references/")
                lines.append(f"- [{Path(target).stem}](<{target}>)")
    lines.extend([
        "", "Select only modules relevant to the intended assistant; preserve canonical behavioral ownership and explicit activation conditions.",
        f"The runtime package's historical manifest version/status is unchanged and is **not** the {platform} skill adapter version.",
        "", "## Source verification", "",
        "`SOURCE_MAP.json` records original canonical paths and SHA-256 hashes of the bytes included here.", "",
    ])
    return "\n".join(lines).encode("utf-8")


def assemble_references(platform: str, version: str) -> dict[str, bytes]:
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+(?:(?:-dev(?:\.[0-9]+)?)|(?:-rc\.[0-9]+))?", version):
        raise BuildError("Invalid adapter version; use 0.1.0-dev, 1.1.0-rc.1 or 1.1.0")
    entries = allowed_entries()
    files: dict[str, bytes] = {}
    tracked = []
    for entry in entries:
        source = entry["source"]
        content = read_source(source)
        files[entry["target"]] = content
        tracked.append({"source": source, "bundled": entry["target"], "role": entry["role"], "sha256": sha256(content)})
    for name in ("BUILDER_CONTRACT.md", "OUTPUT_CONTRACT.md"):
        files[f"references/{name}"] = read_source(f"platforms/shared/{name}")
    files["references/BUILDER_INDEX.md"] = reference_index(entries, platform)
    commit = source_commit()
    files["references/SOURCE_MAP.json"] = (json.dumps({
        "adapter": platform,
        "skill": SKILL_NAME,
        "adapter_version": version,
        "source_commit": commit,
        "source_commit_verification": "clean-git-HEAD" if commit else "unavailable-from-snapshot-or-dirty-worktree",
        "runtime_material_use": "reference-only-for-generated-assistants",
        "source_files": tracked,
    }, indent=2, sort_keys=True) + "\n").encode("utf-8")
    return files


def validate_paths(files: dict[str, bytes]) -> None:
    if "SKILL.md" not in files:
        raise BuildError("Missing SKILL.md")
    check_frontmatter(files["SKILL.md"].decode("utf-8"))
    approved = {"SKILL.md", "references/BUILDER_CONTRACT.md", "references/OUTPUT_CONTRACT.md",
                "references/BUILDER_INDEX.md", "references/SOURCE_MAP.json"}
    for path in files:
        safe_relative(path)
        if path not in approved and not (path.startswith("references/builder/") or path.startswith("references/runtime/")):
            raise BuildError(f"Not an approved skill file path: {path}")
        if not path.endswith((".md", ".json", ".txt")):
            raise BuildError(f"Unexpected file type in installable skill: {path}")
    for origin in ("SKILL.md", "references/BUILDER_INDEX.md"):
        text = files[origin].decode("utf-8")
        for link in re.findall(r"\]\(<?([^)>]+)>?\)", text):
            if "://" in link or link.startswith("#"):
                continue
            if link.startswith("/") or ".." in PurePosixPath(link).parts or "\\" in link:
                raise BuildError(f"Unsafe relative link: {link}")
            destination = (PurePosixPath(origin).parent / link).as_posix()
            if destination not in files:
                raise BuildError(f"Broken skill link in {origin}: {link}")


def make_zip(path: Path, files: dict[str, bytes], prefix: str = "") -> str:
    validate_paths(files)
    if prefix:
        safe_relative(prefix.removesuffix("/"))
        if not prefix.endswith("/"):
            raise BuildError("Archive prefix must end in /")
    path.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(path, "w", compression=ZIP_DEFLATED, compresslevel=9, strict_timestamps=True) as bundle:
        for name, content in sorted(files.items()):
            info = ZipInfo(prefix + name, FIXED_TIMESTAMP)
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            bundle.writestr(info, content, compress_type=ZIP_DEFLATED, compresslevel=9)
    digest = sha256(path.read_bytes())
    (path.parent / (path.name + ".sha256")).write_text(f"{digest}  {path.name}\n", encoding="utf-8")
    return digest
