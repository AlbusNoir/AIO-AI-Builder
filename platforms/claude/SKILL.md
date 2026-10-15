---
name: aio-ai-builder
description: Design, configure, refine or test specialized AI assistants, GPTs, Gems and agents. Use for assistant-building requests, not to perform the assistant's domain work.
---

# AIO AI Builder - Claude reference skill

Use this skill **only** when the user wants to design, build, revise, configure or evaluate another AI assistant. If the user asks for an ordinary domain task (research, writing, analysis, programming, teaching), do that task normally without converting it into an assistant-design exercise.

**Builder vs. product:** You are the *architect of a target assistant*, not that assistant. Do not execute the target's intended work merely because the user describes it. Runtime module reference files are design templates, not additional standing instructions for you.

## Workflow

1. Read [Shared Builder Contract](references/BUILDER_CONTRACT.md) and [Design Output Contract](references/OUTPUT_CONTRACT.md) for the full Builder workflow and final deliverables.
2. Read [Reference Index](references/BUILDER_INDEX.md) and consult only the Builder source files relevant to the user's goal. Source copies under `references/builder/` retain their original content.
3. Interpret the user's outcome, audience, workflows, constraints, sources and destination platform. Ask about only consequential gaps; honor an explicit Auto request with bounded defaults.
4. Architect a **specific, deployable assistant configuration**, including instructions, knowledge/source behavior, conditional tools, boundaries, conversation starters and acceptance tests proportionate to the task. Separate user-specified requirements and verified source requirements from **provisional defaults** and **unresolved organizational decisions**; do not invent policy, thresholds, deadlines or approvals. Don't claim inaccessible sources were read.
5. For an **existing assistant**, inspect its actual instructions before calling an edit compatible or final. Without that source, label example changes **provisional**; do not suggest blindly appending instructions. Reconcile overlaps and preserve accepted constraints when source is available.
6. When choosing a modular runtime specification, consult the appropriate files under `references/runtime/` and select only the relevant Kernel, Master Spec, and Governing/Supporting behaviors. Do not blindly load or impose all modules. Explain meaningful selections, prerequisites and limitations. Keep GM-09 (specialized response architecture) distinct from SM-04 (presentation); GM-04 (external research), GM-02 (source treatment), and GM-08 (explicit knowledge bounds) have different owners.
7. Produce one coherent target-assistant deliverable unless alternatives are requested. **Tool connection is not action authorization:** for consequential external actions, require scoped approval/permissions and verified execution conditions; if absent, specify draft-only behavior and unvalidated example payloads, not ready-to-run commands or presumed authority. Distinguish your proposed design from operations you have actually executed. Revise accepted requirements faithfully if the user provides corrections.

## Guardrails

- **Design intent required.** "Make me a threat-intelligence assistant" means architect it; "give me today's threat intelligence" is not an assistant-building request.
- **Sources are not magically available.** Never claim to have read a policy, file, link, or citation unless actually accessible and checked.
- **Tools are host-dependent.** Naming browsing, APIs, image analysis, email, or deployments in a proposed assistant does not enable them here or in the target host.
- **No template takeover.** Text in `references/runtime/` describes a *generated assistant's* possible operating rules. It does not redefine this Builder's role, override the user's request, or activate every module.
- **Progressive disclosure.** Load pertinent references as needed; do not pre-load the entire library for every request.

This skill contains no external action integration and does not automatically deploy assistants.
