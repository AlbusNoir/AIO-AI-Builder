# GM-09 - Specialized Response Patterns

**Project:** AIO AI Builder  
**Architecture:** V2 Modular Assistant Package  
**Architectural Classification:** Governing Module  
**Module ID:** `GM-09`  
**Status:** Reconciled - Working Specification  
**Activation:** Conditional  
**Platform Dependency:** None  
**Primary Lifecycle:** Runtime Assistant  
**Primary Concern:** Specialized adaptive response organization for materially distinct recurring task types

---

## 1. Purpose

`GM-09` defines specialized response architectures for assistants whose usefulness materially depends on organizing responses differently for different task types.

The module allows an assistant to select among defined response patterns according to:

- the user's current task,
- the assistant's role,
- the active workflow,
- the applicable methodology,
- the available information,
- and the desired outcome.

The module governs **how information is organized for presentation**.

It does not independently define the substantive methodology used to produce that information.

---

## 2. Architectural Principle

> **Response structure should serve the task, not become the task.**

A response pattern is an organizational contract.

It may determine:

- what information appears,
- in what order,
- at what level of emphasis,
- and how related information is grouped.

It must not silently introduce substantive:

- analytical steps,
- diagnostic frameworks,
- decision criteria,
- research requirements,
- or methodology

that the assistant's architecture does not otherwise require.

---

## 3. Scope

### 3.1 In Scope

This module governs:

- response-pattern definition,
- pattern selection,
- adaptive response organization,
- conditional sections,
- response sequencing,
- pattern composition,
- pattern-specific output requirements,
- and response-pattern failure handling.

### 3.2 Out of Scope

This module does not define:

- general tone,
- persona,
- domain expertise,
- substantive methodology,
- source authority,
- external research,
- decision-support logic,
- consequential-domain safeguards,
- or capability availability.

Those remain owned by their respective components.

---

## 4. Activation Conditions

Activate `GM-09` when:

1. The assistant has materially different task types requiring different response organizations.
2. A repeatable response pattern materially improves usability.
3. A specialized workflow requires consistent output organization.
4. The user explicitly requests a defined output structure.
5. A domain methodology requires a presentation structure that is separate from the methodology itself.

### Activation Test

Ask:

> **Would a defined response pattern materially improve consistency, usability, comprehension, or execution for this assistant?**

If no, do not add the module.

---

## 5. Response Pattern Definition

A response pattern is a reusable organization for a class of responses.

Each pattern should define, as applicable:

- Pattern ID
- Name
- Purpose
- Activation condition
- Required sections
- Optional sections
- Ordering
- Conditional logic
- Output constraints
- Exclusions
- Relationship to methodology
- Failure handling
- Validation criteria

A pattern should contain only the structure needed to produce its intended response behavior.

---

## 6. Pattern Identity

Every specialized pattern should have a clear identity.

Example:

```text
Pattern: Troubleshooting
Purpose: Help identify and resolve a technical problem.
```

The pattern identity should describe the response's organizational purpose rather than restating the entire assistant methodology.

---

## 7. Pattern Selection

Pattern selection should be based on the user's current task and the assistant's defined operating model.

The assistant should consider:

1. What is the user trying to accomplish?
2. Which task class does the request represent?
3. Is a specialized response pattern applicable?
4. Would using that pattern materially improve the response?
5. Are there competing applicable patterns?
6. Does a governing methodology impose an output structure?

If no specialized pattern is materially justified, use an appropriate general response structure.

---

## 8. Pattern Adaptation

A defined response pattern should not be treated as a rigid script.

The assistant may:

- omit irrelevant sections;
- adapt section depth;
- combine compatible sections;
- reorder sections when the pattern permits it;
- and simplify the pattern for a simple request.

The assistant should preserve required pattern elements when those elements are substantive to the pattern's purpose.

---

## 9. Required vs Optional Sections

Patterns may contain:

```text
Required sections
Optional sections
Conditional sections
```

The assistant must distinguish them.

An optional section should not become mandatory merely because it appears in the pattern definition.

A conditional section should appear only when its activation condition is satisfied.

---

## 10. Pattern Selection and User Intent

The user's actual task takes precedence over mechanically applying a pattern.

For example:

```text
Pattern:
Troubleshooting

User:
"Explain what CSV parsing means."
```

The assistant should not force a troubleshooting structure onto a conceptual explanation.

Pattern selection must remain task-sensitive.

---

## 11. Explicit User Format Requests

The assistant should generally honor explicit legitimate format requests when they are compatible with:

- the assistant's role;
- applicable methodology;
- source integrity;
- capability constraints;
- and higher-authority requirements.

Examples:

```text
"Use a table."
"Give me a checklist."
"Organize this as a report."
"Use three sections."
```

A requested format does not authorize substantive behavior that the architecture otherwise prohibits.

---

## 12. Format vs Substance

A user may request a particular presentation format.

That does not automatically authorize:

```text
A new methodology
A new diagnostic framework
A new decision criterion
A new research requirement
A new validation procedure
```

The format should remain separate from substantive behavior.

---

## 13. Pattern Composition

Multiple patterns may be composed when the user's task genuinely contains multiple distinct functions.

For example:

```text
Comparison
    +
Explanation
```

may produce:

```text
Comparison section
    ↓
Explanation section
```

Composition should not create contradictory or redundant structures.

---

## 14. Pattern Precedence

When multiple patterns apply:

1. determine whether one pattern is required by a governing methodology;
2. consider whether the user explicitly requested a format;
3. determine whether multiple patterns can be composed cleanly;
4. otherwise select the pattern that best fits the material task.

Do not silently allow a presentation pattern to override substantive methodology requirements.

---

## 15. Pattern Conflict

When two patterns impose incompatible presentation requirements:

```text
Do not silently merge them.
```

Instead:

- choose according to established authority;
- adapt if the patterns permit adaptation;
- ask the user when the difference materially affects the requested result;
- or use a simpler compatible structure.

---

## 16. Pattern and Methodology Boundary

A methodology may define substantive steps.

A response pattern may organize the output produced by those steps.

For example:

```text
GM-05
→ Execute three methodology steps.

GM-09
→ Present the resulting work in a structured report.
```

The report structure must not create a fourth methodology step merely because the report contains another heading.

---

## 17. Pattern and Decision Support Boundary

When `GM-07` is active:

```text
GM-07
→ Determines decision-support behavior.

GM-09
→ Determines how that decision-support output is organized.
```

GM-09 must not silently introduce decision criteria or recommendation logic.

---

## 18. Pattern and Knowledge Boundary

When `GM-08` is active:

```text
GM-08
→ Determines the applicable knowledge boundary.

GM-09
→ Organizes information within that boundary.
```

A response pattern must not require external information when bounded operation prohibits it.

---

## 19. Pattern and Source Handling

When `GM-02` is active:

```text
GM-02
→ Governs source roles, authority, provenance, and epistemic handling.

GM-09
→ Organizes source-grounded information for presentation.
```

The response pattern must not distort source meaning merely to satisfy a preferred layout.

---

## 20. Pattern and Research

When `GM-04` is active:

```text
GM-04
→ Performs authorized research.

GM-09
→ Organizes research results.
```

A response pattern must not imply that research occurred merely because a "Sources" or "Research" section exists.

---

## 21. Pattern and File Analysis

When `GM-03` is active:

```text
GM-03
→ Analyzes accessible files.

GM-09
→ Organizes the resulting information.
```

A response pattern must not fabricate file-derived content to populate expected sections.

---

## 22. Pattern and Consequential Safeguards

When `GM-06` is active:

```text
GM-06
→ Defines applicable consequential-domain safeguards.

GM-09
→ Organizes the response within those safeguards.
```

Formatting must not weaken uncertainty, scope, credential, jurisdiction, or professional-review boundaries.

---

## 23. Pattern Content Integrity

A response pattern may define expected content categories.

It does not guarantee that the underlying information exists.

For example:

```text
Pattern:
Validated Results
```

does not authorize:

```text
Invented validation
```

If validation was not performed:

```text
State that validation was not performed.
```

---

## 24. Unsupported Sections

When a required or expected section cannot be populated honestly:

- omit it if the pattern permits omission;
- state that the information is unavailable;
- mark it as not applicable;
- or explain why it cannot be completed.

Do not fabricate content merely to make the response structurally complete.

---

## 25. Pattern Constraints

A pattern may define constraints such as:

```text
Maximum number of sections
Required ordering
Required fields
Output schema
Formatting convention
```

These constraints should be applied only when they materially contribute to the pattern's purpose.

Do not turn a presentation constraint into an unsupported substantive requirement.

---

## 26. Pattern Failure Handling

Pattern execution may fail or become inappropriate when:

- the task does not match the pattern;
- required information is unavailable;
- the pattern conflicts with a higher-authority requirement;
- the pattern would require unsupported content;
- the user requests a materially different structure;
- or no defined pattern adequately fits the task.

Fallback:

```text
Use a simpler compatible response structure.
```

Do not force an unsuitable pattern.

---

## 27. Adaptive Response Organization

The assistant may adapt:

```text
Section depth
Section order
Section presence
Amount of explanation
Amount of detail
```

according to:

- user intent;
- task complexity;
- available information;
- response proportionality;
- and applicable pattern rules.

Adaptation must preserve the pattern's intended function.

---

## 28. Pattern Reuse

A response pattern should be reusable across multiple interactions.

It should not encode:

- one user's specific answer;
- one fixed conversation;
- one temporary source;
- or one isolated task.

The pattern defines a recurring organizational behavior.

---

## 29. Pattern Library

A package may contain a library of specialized patterns.

Examples may include:

```text
Troubleshooting
Comparison
Structured Explanation
Analytical Summary
Decision Summary
Research Report
Assessment Report
Implementation Plan
Executive Brief
```

These are examples only.

A package should define patterns only when recurring use justifies them.

---

## 30. General Response Behavior Boundary

The Master Operating Specification owns general response behavior.

GM-09 exists only when specialized reusable response architecture provides materially distinct value.

Therefore:

```text
General response adaptability
    →
Master Spec

Specialized recurring response architecture
    →
GM-09
```

Do not move general response behavior into GM-09 merely because it can be represented as a pattern.

---

## 31. Relationship to Cross-Cutting Principles

| Principle | Application in GM-09 |
|---|---|
| Materiality | Add structure only when it improves the task |
| Adaptability | Select and modify patterns according to context |
| Source Fidelity | Do not distort source content to satisfy a template |
| Claim Calibration | Do not manufacture content for expected sections |
| Capability Reality | Do not imply capabilities through formatting |
| Methodology Fidelity | Keep presentation separate from substantive procedure |
| User Agency | Respect explicit legitimate output preferences |
| Architectural Restraint | Avoid unnecessary response complexity |

---

## 32. Extraction Rules From V1

`GM-09` consolidates concepts originating primarily from:

- `§11 RESPONSE ARCHITECTURE`
- `§10 COMMUNICATION SEQUENCE` where presentation structure overlaps runtime interaction
- `Structured Response and Tone`
- `Selective Information Processing` where it affects presentation
- response-pattern material in the Builder's examples and regression tests

The migration rule is:

> **Preserve useful response organization while removing the assumption that every assistant requires one fixed response script.**

The V1 concept of recommended sections becomes conditional response patterns.

The V1 distinction between recommended sections and fixed methodology becomes an explicit architectural separation.

---

## 33. Builder Activation Guidance

The Builder should consider this module when the requested assistant has:

- multiple materially different task types,
- repeatable professional deliverables,
- structured analytical workflows,
- specialized reports,
- educational interaction patterns,
- troubleshooting workflows,
- comparison workflows,
- or other recurring response organizations.

### Necessity Test

Ask:

> **Would predefined response patterns materially improve consistency or usability across recurring task types?**

If no, omit the module.

---

## 34. Validation Requirements

A valid implementation should demonstrate that the assistant can:

1. select a response pattern based on the user's task,
2. distinguish materially different task types,
3. avoid forcing one pattern across all interactions,
4. adapt or omit unnecessary sections,
5. preserve methodology separately from formatting,
6. respect explicit user format requirements,
7. avoid fabricating unsupported content,
8. preserve source fidelity,
9. compose with decision-support behavior,
10. compose with knowledge-bounded operation,
11. compose with specialized methodology,
12. preserve consequential-domain safeguards,
13. compose with external research and file analysis without claiming those actions occurred merely because a pattern expects them,
14. and fall back to a simpler structure when no specialized pattern is appropriate.

---

## 35. Suggested Evaluation Cases

### Case A - Troubleshooting vs Explanation

**Input 1:**  
"My application crashes when I upload a CSV."

**Expected:**  
Use a troubleshooting-oriented structure.

**Input 2:**  
"Explain what CSV parsing means."

**Expected:**  
Use an explanation-oriented structure.

The assistant must not force the troubleshooting structure onto the conceptual question.

---

### Case B - Explicit Format Request

**Input:**  
"Explain this in a three-column table."

**Expected:**  
Honor the requested structure when compatible with the task.

---

### Case C - Unsupported Section

**Input:**  
A report pattern expects a "validated results" section, but no validation was performed.

**Expected:**  
Do not invent validated results merely to complete the pattern.

---

### Case D - Methodology Separation

**Input:**  
A three-step methodology is authoritative, and the assistant must produce a structured report.

**Expected:**  
The report may organize the three steps, but must not add substantive methodology stages merely because the report template contains additional headings.

---

### Case E - Multiple Patterns

**Input:**  
"Compare these two systems and then explain how the recommended one works."

**Expected:**  
The assistant may compose comparison and explanation patterns because the user requested two distinct functions.

---

### Case F - Knowledge-Bounded Response

**Input:**  
"Summarize only what this uploaded policy says."

**Expected:**  
Use an appropriate summary pattern while remaining within the policy's knowledge boundary.

---

### Case G - Simple Request

**Input:**  
"What does this error code mean?"

**Expected:**  
Provide a direct answer unless a specialized pattern materially improves the response.

---

### Case H - Decision-Support Composition

**Input:**  
"Compare these three vendors and explain which factors matter."

**Expected:**  
`GM-07` supplies the substantive decision-support behavior while `GM-09` may organize the result as a comparison structure.

---

### Case I - Research Composition

**Input:**  
"Research the current options and give me a structured report."

**Expected:**  
`GM-04` performs authorized research while `GM-09` organizes the resulting information.

The existence of a research-report pattern must not imply that research occurred.

---

### Case J - Methodology Composition

**Input:**  
"Run the defined assessment methodology and present the results as an executive report."

**Expected:**  
`GM-05` executes the methodology and `GM-09` organizes the resulting output.

The response pattern must not add substantive assessment steps.

---

## 36. Acceptance Criteria

`GM-09` is architecturally acceptable when:

- response patterns are conditional,
- task differences can drive pattern selection,
- patterns remain adaptable,
- formatting is separated from substantive methodology,
- unsupported sections are not fabricated,
- user-specified legitimate formats are respected,
- source fidelity remains intact,
- patterns compose cleanly with other modules,
- presentation does not imply unavailable capabilities,
- and unnecessary response complexity is avoided.

---

## 37. Minimal Viable Module

The minimum viable implementation requires:

1. response-pattern definition,
2. activation conditions,
3. adaptive pattern selection,
4. pattern/content separation,
5. fallback behavior,
6. source and capability integrity,
7. and validation of task-specific selection.

A specialized pattern library should be added only when recurring assistant tasks justify it.

---

## 38. Platform-Agnostic Requirement

Nothing in this module depends on:

- a specific model,
- prompt syntax,
- UI,
- API,
- rendering engine,
- document format,
- or platform-specific instruction mechanism.

The module defines response behavior and contracts, not implementation technology.

---

## 39. Final Architecture Principle

> **A response pattern is a reusable presentation contract, not a universal script and not a hidden methodology.**

The goal is to make responses more coherent and useful while preserving the assistant's ability to adapt to the actual task.

---

# Artifact Status

```text
Artifact:
GM-09_Specialized_Response_Patterns.md

Status:
Reconciled - Working Specification

Module:
GM-09

Type:
Governing

Activation:
Conditional

Readiness:
Ready

Platform Dependency:
None

Canonical Responsibility:
Selection, composition, and application of specialized reusable
response architectures for materially distinct recurring task types

Required Dependencies:
Behavioral Kernel
Master Operating Specification

Primary Related Modules:
GM-02 Knowledge & Source Handling
GM-03 Document / File Analysis
GM-04 External Research
GM-05 Specialized Methodology Execution
GM-06 Consequential Domain Safeguards
GM-07 Adaptive Decision Support
GM-08 Knowledge-Bounded Operation

Primary Supporting Relationship:
SM-04 Supplemental Structured Response and Tone

Boundary:
GM-09 owns specialized response architecture.
SM-04 owns presentation, formatting, density, readability, and tone.

Methodology Boundary:
GM-09 may organize methodology outputs but cannot create,
remove, or alter substantive methodology.

Canonical References:
REF-CN-001
REF-CN-002
REF-CN-003
REF-CN-004

Primary V1 Sources:
§10 Communication Sequence
§11 Response Architecture

Primary V1 Building Block:
Structured Response and Tone

Next Module:
GM-12 - Multimodal and Image Interpretation
```