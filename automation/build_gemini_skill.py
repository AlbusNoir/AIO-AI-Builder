#!/usr/bin/env python3
"""Build deterministic Gemini Apps and Gemini CLI AIO AI Builder skill bundles.

Only approved canonical source files and the Gemini SKILL.md are distributed.
The package is an assistant *Builder*, not an autonomous domain assistant.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from platform_skill_common import (
    BuildError, REPO, SKILL_NAME, assemble_references, check_frontmatter,
    make_zip, read_source, validate_paths,
)

DEFAULT_VERSION = "0.1.3-dev"


def build_files(version: str = DEFAULT_VERSION) -> dict[str, bytes]:
    files = assemble_references("gemini", version)
    files["SKILL.md"] = read_source("platforms/gemini/SKILL.md")
    validate_paths(files)
    return files


def build_artifacts(output_dir: Path, version: str = DEFAULT_VERSION) -> dict[str, Path]:
    files = build_files(version)
    apps_zip = output_dir / f"AIO-AI-Builder-Gemini-Apps-Skill-{version}.zip"
    cli_skill = output_dir / f"AIO-AI-Builder-Gemini-CLI-Skill-{version}.skill"
    make_zip(apps_zip, files)
    make_zip(cli_skill, files, prefix=f"{SKILL_NAME}/")
    return {"apps": apps_zip, "cli": cli_skill}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=REPO / "dist")
    parser.add_argument("--adapter-version", default=DEFAULT_VERSION)
    args = parser.parse_args()
    try:
        results = build_artifacts(args.output_dir, args.adapter_version)
    except (BuildError, ValueError, KeyError, OSError, UnicodeError) as error:
        parser.exit(2, f"Gemini skill build FAILED: {error}\n")
    for surface, file in results.items():
        print(f"Gemini {surface} artifact: {file}\n  checksum: {file}.sha256")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
