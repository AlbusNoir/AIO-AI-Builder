#!/usr/bin/env python3
"""Build a reproducible, skills-only portable ChatGPT Agent Plugin archive.

The build reuses cross-platform allowlisted Builder/runtime references verbatim.
No MCP server, scripts, hooks, credentials or canonical package modification.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from platform_skill_common import (
    BuildError, FIXED_TIMESTAMP, REPO, SKILL_NAME, assemble_references,
    read_source, safe_relative, sha256, validate_paths,
)

DEFAULT_VERSION = "0.1.0-dev"
PLUGIN_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
PLUGIN_NAME = "aio-ai-builder"
SKILL_DIR = f"skills/{SKILL_NAME}/"


def read_manifest(version: str) -> bytes:
    """Validate minimal portable metadata; override only adapter version."""
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+(?:(?:-dev(?:\.[0-9]+)?)|(?:-rc\.[0-9]+))?", version):
        raise BuildError("Invalid adapter version; expected e.g. 0.1.0-dev or 1.1.0-rc.1")
    try:
        manifest = json.loads(read_source("platforms/chatgpt/plugin.json"))
    except (ValueError, UnicodeError) as error:
        raise BuildError(f"Invalid plugin.json: {error}") from error
    if not isinstance(manifest, dict):
        raise BuildError("Plugin manifest must be an object")
    if manifest.get("$schema") != PLUGIN_SCHEMA or manifest.get("name") != PLUGIN_NAME:
        raise BuildError("Invalid portable plugin schema or stable plugin identifier")
    if set(manifest) != {"$schema", "name", "version", "description", "keywords", "extensions"}:
        raise BuildError("Unexpected root fields in skills-only plugin manifest")
    if manifest.get("version") != DEFAULT_VERSION:
        raise BuildError("Manifest source baseline version mismatch")
    if not isinstance(manifest.get("description"), str) or not 15 <= len(manifest["description"]) <= 4000:
        raise BuildError("Missing/invalid plugin description")
    if not isinstance(manifest.get("keywords"), list) or not all(isinstance(x, str) and x for x in manifest["keywords"]):
        raise BuildError("Invalid plugin keywords")
    if set(manifest["extensions"]) != {"com.openai"}:
        raise BuildError("Unexpected plugin namespace")
    openai = manifest["extensions"]["com.openai"]
    if not isinstance(openai, dict) or set(openai) != {"interface"}:
        raise BuildError("Only OpenAI presentation metadata is permitted")
    interface = openai["interface"]
    required = {"displayName", "shortDescription", "longDescription"}
    if not isinstance(interface, dict) or set(interface) != required or not all(
        isinstance(interface[x], str) and interface[x].strip() for x in required
    ):
        raise BuildError("Invalid presentation metadata")
    manifest["version"] = version
    return (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def build_files(version: str = DEFAULT_VERSION) -> dict[str, bytes]:
    """Return ZIP-relative files, rejecting unapproved or unsafe content."""
    skill_files = assemble_references("chatgpt", version)
    skill_files["SKILL.md"] = read_source("platforms/chatgpt/SKILL.md")
    validate_paths(skill_files)
    plugin_files = {"plugin.json": read_manifest(version)}
    for name, content in skill_files.items():
        path = SKILL_DIR + name
        safe_relative(path)
        plugin_files[path] = content
    validate_plugin_files(plugin_files)
    return plugin_files


def validate_plugin_files(files: dict[str, bytes]) -> None:
    if "plugin.json" not in files or SKILL_DIR + "SKILL.md" not in files:
        raise BuildError("Missing required plugin manifest or skill entry point")
    if len(files) != 44:
        raise BuildError("Unexpected plugin file inventory (expect 1 manifest + 43 skill files)")
    if any(name != "plugin.json" and not name.startswith(SKILL_DIR) for name in files):
        raise BuildError("Unauthorized file outside the single portable plugin skill")
    skill_files = {name.removeprefix(SKILL_DIR): body for name, body in files.items() if name != "plugin.json"}
    validate_paths(skill_files)
    for name, content in files.items():
        safe_relative(name)
        if not isinstance(content, bytes):
            raise BuildError(f"Non-byte plugin file: {name}")
        if name != "plugin.json" and not name.endswith((".md", ".txt", ".json")):
            raise BuildError(f"Unexpected file type: {name}")
    try:
        obj = json.loads(files["plugin.json"])
    except ValueError as error:
        raise BuildError(f"Malformed output manifest: {error}") from error
    if obj.get("name") != PLUGIN_NAME or obj.get("$schema") != PLUGIN_SCHEMA:
        raise BuildError("Plugin name/schema changed in generated file")
    if obj.get("mcpServers") or "mcp.json" in files or any(".codex-plugin" in p for p in files):
        raise BuildError("Unexpected MCP server or compatibility overlay")
    for denied in (".git/", "tests/", "automation/", "architecture/", ".env", "results/"):
        if any(denied in p for p in files):
            raise BuildError(f"Private/non-distributable path: {denied}")


def build_artifact(output_dir: Path, version: str = DEFAULT_VERSION) -> Path:
    files = build_files(version)
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / f"AIO-AI-Builder-ChatGPT-Plugin-{version}.zip"
    with ZipFile(target, "w", compression=ZIP_DEFLATED, compresslevel=9, strict_timestamps=True) as bundle:
        for name, content in sorted(files.items()):
            info = ZipInfo(name, FIXED_TIMESTAMP)
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            bundle.writestr(info, content, compress_type=ZIP_DEFLATED, compresslevel=9)
    digest = sha256(target.read_bytes())
    (output_dir / f"{target.name}.sha256").write_text(f"{digest}  {target.name}\n", encoding="utf-8")
    return target


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=REPO / "dist")
    parser.add_argument("--adapter-version", default=DEFAULT_VERSION)
    args = parser.parse_args()
    try:
        archive = build_artifact(args.output_dir, args.adapter_version)
    except (BuildError, ValueError, KeyError, OSError, UnicodeError) as error:
        parser.exit(2, f"ChatGPT plugin build FAILED: {error}\n")
    print(f"ChatGPT plugin artifact: {archive}\n  checksum: {archive}.sha256")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
