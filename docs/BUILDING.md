# Building AIO AI Builder v1.1.0 from Public Source

## Requirements

Python 3.13+ and a standard shell (PowerShell, bash or equivalent). Network access, Gemini model credentials and the private Gitea source tree are not required to run the public deterministic checks and build scripts.

From the root of this repository:

```bash
python run_tests.py
python tests/08_package_contract/package_contract.py
python tests/09_v2_behavioral/run_static_contract.py
python automation/build_releases.py --all --adapter-version 1.1.0
```

The unified runner re-runs the three public checks, builds two independent copies of each adapter and verifies matching archive digests, file allowlists and `.sha256` files. Outputs:

```text
dist/release-stage/
  AIO-AI-Builder-ChatGPT-Plugin-1.1.0.zip
  AIO-AI-Builder-Claude-Skill-1.1.0.zip
  AIO-AI-Builder-Gemini-Apps-Skill-1.1.0.zip
  AIO-AI-Builder-Gemini-CLI-Skill-1.1.0.skill
  [one .sha256 next to each archive]
  SHA256SUMS.txt
  build-manifest.json
  build-report.md
```

`--replace` may replace only a runner-owned stage; unrecognized destinations are protected. You can supply `--output-dir` to use a new location. Use `--skip-tests` only if the three public checks have **already** passed; that option explicitly records tests as not run by the staging command.

## The canonical runtime package

`package/` is the canonical, platform-agnostic runtime material. It is included in this source distribution as complete reference files. You may package the directory yourself for use as knowledge/instructions, taking care to preserve its contents. The unified adapter runner does **not** construct the official canonical package-only release archive; that archive remains a separate official release artifact.

## What the public test results mean

`run_tests.py` runs the selected platform packaging and shared-design unit tests; package/static scripts validate source and structure. These checks are not the historical 46-case live Custom GPT acceptance, do not call a hosted model, and do not establish successful installation on a specific destination platform.

The public source may be committed to an independent GitHub repository or checked out as a working copy without `.git/`. If committed and clean, the build's generated source map may record that **public** commit SHA; otherwise it may report no verifiable commit. Consequently, local archive hashes can differ from the official Gitea-published archives even when the functional content is equivalent. Do not represent them as official release assets.

The public `pyproject.toml` removes dependencies used only by the maintainer's private model-testing harness; `uv.lock` is omitted as unnecessary for these standard-library-only scripts.
