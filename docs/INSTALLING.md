# Using the Public AIO AI Builder Source

## Choose the artifact for your host

Run the build command in [BUILDING.md](BUILDING.md), then examine `dist/release-stage/`:

| Host | Produced file | Contents and intended use |
|---|---|---|
| ChatGPT | `AIO-AI-Builder-ChatGPT-Plugin-1.1.0.zip` | Skills-only plugin archive with `plugin.json` and `skills/aio-ai-builder/` |
| Claude | `AIO-AI-Builder-Claude-Skill-1.1.0.zip` | Skill archive rooted at `aio-ai-builder/` |
| Gemini Apps | `AIO-AI-Builder-Gemini-Apps-Skill-1.1.0.zip` | Skill and reference files intended for Gemini-compatible app setup |
| Gemini CLI | `AIO-AI-Builder-Gemini-CLI-Skill-1.1.0.skill` | ZIP-format skill archive with `aio-ai-builder/` root |

Host installation and supported upload formats differ across products, plans and deployments. Consult your host's current instructions before importing or extracting an archive. **Do not assume every host supports direct ZIP import or the `.skill` suffix.** If a host has no direct import mechanism, its editable instructions and knowledge interfaces may require manual configuration using the included skill and reference documents.

The four adapters describe assistant-design behavior; they do not include an MCP server, tool credentials, live integrations, or permission to take consequential external actions. An imported package still depends on the host's capabilities and user configuration.

## Canonical generated-assistant runtime reference

The `package/` directory is separate from the four Builder adapters. It supplies the Kernel, Master Spec, Governing/Supporting Modules, and canonical references for *assistants the Builder designs*. Do not use the entire runtime module collection as a replacement for the Builder's own instructions or activate all modules by default.

## Verification

The build creates `.sha256` files and a `SHA256SUMS.txt` for its **local** outputs; verify these before transferring artifacts. A successful checksum demonstrates byte integrity of the local build output, not host installation, official origin, or behavioral acceptance.
