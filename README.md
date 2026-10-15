# AIO AI Builder

**Public source distribution for stable release v1.1.0.**

AIO AI Builder is a modular framework for designing purpose-built AI assistants. The **Builder** designs other assistants; it does not automatically install them, grant tools, or execute their future work.

This repository contains an independently rebuildable snapshot of the MIT-licensed project. It is a **curated source distribution**, not the private development repository or a two-way Git mirror. Users are welcome to clone and fork the source and maintain their own derivatives. Upstream development is independently maintained; this repository does **not** accept pull requests or run an external contribution program.

## What is included

- `package/` - platform-agnostic generated-assistant runtime references, Kernel bootstrap, Master Operating Specification, 11 governing and 11 supporting modules, canonical contracts.
- `knowledge/` - approved Builder design references.
- `platforms/` - ChatGPT Plugin, Claude Skill, Gemini Apps and Gemini CLI Skill sources, plus shared Builder contract.
- `automation/` - standard-library-only adapter builders and selected public build tests.
- `tests/` - static and package-contract validation scripts, **not** private live/model acceptance corpora.
- `PUBLIC_SOURCE_MANIFEST.json` - per-file SHA-256 hashes for this export; see the provenance note below.

## Requirements

- Python 3.13 or later. All public build/test scripts use the Python standard library; no API credentials, private development files, or third-party Python packages are required.
- Optional: `uv`, if you prefer it to manage a local Python environment. The public snapshot intentionally contains no `uv.lock` because there are no third-party build dependencies.

## Verify and rebuild

From the repository root:

```bash
python run_tests.py
python tests/08_package_contract/package_contract.py
python tests/09_v2_behavioral/run_static_contract.py
python automation/build_releases.py --all --adapter-version 1.1.0
```

The last command runs the public checks, builds four adapter archives, verifies file contents and checksums, and rebuilds them for reproducibility. Artifacts are staged under `dist/release-stage/`. Use `--replace` only when overwriting an intact stage created by that runner.

See [Building from Source](docs/BUILDING.md) and [Installation Guide](docs/INSTALLING.md) for details. The canonical `package/` tree is source material for generated assistants and is deliberately **not** one of the four staged adapter formats.

## Source provenance and release status

This public snapshot corresponds to stable release **v1.1.0**, but uses a new public Git history. Its Git commit SHA therefore differs from the private authoritative repository's commit. Adapter output may contain the *public* checkout's commit provenance or no commit if built outside Git. **Byte-for-byte matching the officially published release archives is not promised.**

`PUBLIC_SOURCE_MANIFEST.json` lists the intended public files and hashes; it is an inventory/integrity aid, not a signature or independent authentication of the source's origin. Official binary releases are distributed separately by the project maintainer; a locally staged archive is not an officially published release.

Structural and deterministic tests do **not** establish successful installation in every host or the reliability of every model response.

## License and maintenance model

Distributed under the [MIT License](LICENSE). Forking, modifying, and redistributing are permitted under its terms. This is a read-only upstream distribution: GitHub Issues, Discussions and Pull Requests are not offered as a route for upstream changes or support.
