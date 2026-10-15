# SM-07 - Supplemental Guided Entry and Conversation Starters

**Architectural Classification:** Supporting Module  
**Module ID:** `SM-07`  
**Status:** Defined  
**Activation:** Conditional  
**Platform Dependency:** None  
**Primary Lifecycle:** Builder / Runtime Assistant  
**Primary Concern:** Helping users understand how to begin using an assistant through optional entry guidance and representative conversation starters

---

## 1. Purpose

`SM-07` defines optional mechanisms for helping a user understand how to begin interacting with an assistant.

It covers:

- conversation starters,
- initial orientation,
- representative first-use prompts,
- lightweight entry guidance,
- and optional thematic introductions.

The module exists to reduce entry friction when an assistant's use is not immediately obvious.

---

## 2. Architectural Principle

> **Make the assistant easy to enter without forcing every user through a scripted opening.**

The assistant may provide useful entry points, but the presence of an entry mechanism does not require a fixed conversation sequence.

The preferred architecture is:

```text
Assistant purpose
        ↓
Representative entry points
        ↓
User chooses what to do
        ↓
Normal interaction begins
```

rather than:

```text
Mandatory greeting
        ↓
Mandatory question
        ↓
Mandatory sequence
        ↓
User may finally interact
```

---

## 3. Architectural Boundary

`SM-07` owns the **entry experience**.

It does not own:

- the fundamental interaction model,
- ongoing engagement,
- persona,
- response tone,
- methodology,
- learning workflows,
- or persistent onboarding state.

Those remain elsewhere.

---

## 4. Scope

### 4.1 In Scope

This module governs:

- conversation starters,
- first-use guidance,
- representative user prompts,
- optional thematic introductions,
- initial orientation,
- and entry-point design.

### 4.2 Out of Scope

This module does not independently define:

- general conversational behavior,
- ongoing engagement,
- user profiling,
- persistent onboarding,
- or mandatory multi-turn workflows.

---

## 5. Activation Conditions

Activate `SM-07` when one or more of the following materially improves usability:

1. The assistant supports several distinct use cases.
2. New users may not know what to ask.
3. The assistant benefits from example prompts.
4. The assistant has a specialized workflow that should be discoverable.
5. The requested experience benefits from thematic orientation.
6. The assistant has important capabilities that are otherwise difficult to discover.

Do not activate the module merely because a greeting is aesthetically appealing.

---

## 6. Entry Necessity Test

Ask:

> **Would a new user materially benefit from guidance about how to begin?**

If no:

```text
No specialized entry module.
```

If yes:

```text
Provide lightweight entry guidance or representative starters.
```

---

## 7. Conversation Starters

Conversation starters should represent useful ways a user can begin interacting with the assistant.

They should be:

- representative,
- actionable,
- understandable,
- aligned with actual capabilities,
- and varied enough to expose important use cases.

They should not imply capabilities the assistant does not possess.

---

## 8. Starter Design

A good starter should answer:

> **What could I actually ask this assistant to do?**

Examples:

```text
"Help me compare these two project approaches."

"Review this document and identify the key requirements."

"Create a practice scenario for this interview."
```

Poor starters are vague:

```text
"Tell me something interesting."

"Use your capabilities."

"Help me."
```

unless the assistant's purpose is intentionally broad.

---

## 9. Representative Coverage

Conversation starters should cover the assistant's most important intended entry points rather than attempting to enumerate every possible task.

For example:

```text
Primary task
Secondary task
Specialized capability
```

may be sufficient.

Do not create dozens of starters simply because the assistant supports dozens of operations.

---

## 10. Capability Integrity

Every starter must correspond to a capability or behavior the assistant can actually perform.

Do not create a starter such as:

```text
"Analyze my spreadsheet and automatically update the database."
```

unless the required capability actually exists.

Entry guidance is part of the assistant's claim surface.

---

## 11. Initial Orientation

Some assistants benefit from a short explanation of:

- what the assistant does,
- what kinds of inputs are useful,
- and what the user can ask for.

Orientation should be proportional to complexity.

### Simple Assistant

A short description may be enough.

### Complex Assistant

A few representative entry paths may be useful.

### Highly Specialized Workflow

A concise explanation of required inputs or first steps may be justified.

---

## 12. Orientation vs Instruction

Orientation tells the **user** how to use the assistant.

Instructions tell the **assistant** how to behave.

Do not confuse:

```text
User-facing orientation
```

with:

```text
Runtime behavioral instruction
```

For example:

```text
User-facing:
"Upload the document you want reviewed."

Assistant behavior:
When an accessible document is provided, analyze relevant content according to GM-03.
```

---

## 13. Optional Thematic Greeting

A thematic greeting may be appropriate when it materially contributes to the intended experience.

Examples from the v1 source include specialized greetings such as:

- "Greetings, Developer"
- "Hello, and welcome to Laundry Buddy..."
- thematic introductions for domain-specific assistants.

The v2 architecture treats these as optional expression rather than universal behavior.

---

## 14. Greeting Restraint

Do not force a thematic greeting when it:

- delays the user's task,
- creates unnecessary friction,
- conflicts with the requested tone,
- becomes repetitive,
- or provides no meaningful orientation.

A specialized assistant can begin directly with useful work.

---

## 15. Direct Entry

When the user's first message already contains a sufficiently clear task, the assistant should normally proceed directly.

For example:

```text
User:
"Review this contract and list the termination provisions."

Expected:
Begin the task.

Not necessary:
"Welcome! I'm your contract analysis assistant. Here are five things you can ask me..."
```

Entry guidance should not obstruct an already clear request.

---

## 16. First-Use Guidance

If the task is underspecified and the assistant genuinely needs user input, entry guidance may help the user understand what information would be useful.

For example:

```text
"Tell me what you're trying to accomplish and any constraints I should preserve."
```

The question should be driven by actual task requirements rather than generic onboarding.

---

## 17. Progressive Disclosure

Do not present every possible capability at first contact.

Prefer:

```text
Core purpose
+
A few useful entry points
```

Then reveal specialized capabilities when relevant.

This reduces cognitive load while preserving discoverability.

---

## 18. Entry Points and Capability Discovery

Conversation starters can expose capabilities that would otherwise be difficult to discover.

For example, an assistant with document and image capabilities might use:

```text
"Review this document for key requirements."

"Analyze this diagram and explain its structure."
```

The starter demonstrates capability without requiring a lengthy capability list.

---

## 19. Conversation Starters vs Communication Sequence

The v1 architecture required a Communication Sequence describing the user's journey.

The v2 architecture separates:

```text
Conversation Starters
        ↓
Optional entry points

Interaction Model
        ↓
Actual runtime interaction behavior
```

A list of starters does not define a mandatory conversation sequence.

---

## 20. Adaptive Entry

If the assistant receives a clear user task immediately, bypass optional onboarding.

If the user appears unsure what to do, provide appropriate orientation.

Thus:

```text
Clear request
→ Execute

Unclear but recoverable
→ Focused clarification

User unsure how to begin
→ Optional entry guidance
```

---

## 21. Entry and User Agency

Conversation starters should invite rather than constrain.

They should not imply:

```text
"You must choose one of these options."
```

unless the assistant genuinely requires a bounded selection.

The user should normally remain free to provide a different request.

---

## 22. Entry and Persona

When `SM-03` is active, persona may influence:

- greeting,
- wording,
- thematic framing,
- or examples.

However, persona should not make entry guidance confusing.

For example, a playful persona may change:

```text
"Tell me what you're building."
```

to:

```text
"Bring me the contraption you're building, and we'll figure out how to make it work."
```

The underlying task remains the same.

---

## 23. Entry and Structured Response

When `SM-04` is active, starter wording may reflect the assistant's preferred interaction style.

However, starter content remains owned by `SM-07`.

---

## 24. Entry and Engagement

When `SM-01` is active:

```text
SM-07
→ helps the user begin

SM-01
→ supports participation after interaction begins
```

Do not duplicate ongoing engagement behavior in the entry module.

---

## 25. Entry and Iterative Adaptation

When `SM-05` is active, later feedback may reveal that initial guidance was insufficient.

For example:

```text
User:
"I didn't know I could upload a spreadsheet."

Later:
The assistant can make the relevant capability more discoverable during interaction.
```

This does not require dynamically rewriting the published conversation starters unless the platform supports such behavior.

---

## 26. Learning Composition

When `GM-13` is active, starters may expose distinct learning paths:

```text
"Give me a beginner practice exercise."

"Quiz me on this topic."

"Run a realistic scenario with me."
```

The starter should expose the learning use case.

The learning architecture remains owned by `GM-13`.

---

## 27. Decision Support Composition

When `GM-07` is active, starters may expose decision-support entry points:

```text
"Help me compare these options."

"Help me identify the tradeoffs in this decision."
```

Do not make a starter imply that the assistant will make the decision for the user.

---

## 28. Document and File Composition

When `GM-03` is active, starters may help users understand that files can be useful inputs.

For example:

```text
"Upload a report and ask me to extract its key requirements."
```

The starter must reflect actual file-access capability.

---

## 29. External Research Composition

When `GM-04` is active, a starter may expose research behavior:

```text
"Research the latest information on this topic and compare reliable sources."
```

Only use such a starter if external research is actually available.

---

## 30. Multimodal Composition

When `GM-12` is active, starters may expose visual workflows:

```text
"Upload an image and ask me to identify the visible elements."

"Show me this chart and ask me to explain its trends."
```

Do not imply visual capabilities that are unavailable.

---

## 31. Knowledge-Bounded Composition

When `GM-08` is active, starters may explicitly communicate source-bounded workflows:

```text
"Ask questions about the documents I've provided."
```

They should not imply unrestricted external knowledge if the intended assistant is source-bounded.

---

## 32. Methodology Composition

When `GM-05` is active, starters may expose methodology-based workflows:

```text
"Apply the approved methodology to this case."
```

The starter should not redefine or summarize the methodology inaccurately.

---

## 33. Consequential Domain Composition

When `GM-06` is active, entry guidance should not create false impressions of professional credentials or guaranteed outcomes.

Avoid:

```text
"Get a definitive diagnosis."

"Get guaranteed legal advice."
```

Prefer descriptions of the actual supported task.

---

## 34. Resource Recommendation Composition

When `GM-14` is active, starters may expose resource-oriented tasks:

```text
"Recommend learning resources for my current skill level."
```

The starter should not imply that recommendations are guaranteed to be optimal.

---

## 35. Selective Information Composition

When `SM-06` is active, starters may demonstrate selective information handling:

```text
"Find the relevant section of this document."

"Give me only the requirements that apply to this project."
```

---

## 36. Reference Guidance Composition

When `SM-02` is active, starters may expose source-navigation behavior:

```text
"Point me to the most relevant section of the documentation."
```

---

## 37. Support and Feedback Composition

When `SM-11` is active, support pathways should not be confused with conversation starters.

For example:

```text
Starter:
"Help me troubleshoot this workflow."

Support:
"Report a problem with the assistant."
```

These serve different purposes.

---

## 38. Political or Civic Entry Guidance

If the assistant is intended for political or electoral information, conversation starters must remain informational rather than persuasive.

Appropriate examples:

```text
"Compare the documented positions of these candidates on housing."

"Summarize the provisions of this ballot measure."

"Explain the arguments supporters and opponents have publicly made."
```

Avoid starters that frame a political choice as already determined or invite hidden persuasion.

---

## 39. Starter Quality Criteria

Each starter should satisfy:

1. **Capability realism** - the assistant can actually perform the implied task.
2. **Outcome alignment** - it represents a meaningful use case.
3. **Clarity** - a new user can understand the intended action.
4. **Specificity** - enough detail to demonstrate usefulness.
5. **Flexibility** - it does not unnecessarily constrain the user's task.
6. **Non-deception** - it does not imply unsupported authority or capability.
7. **Distinctiveness** - it adds a useful entry path rather than duplicating another starter.

---

## 40. Starter Count

There is no universal required number of conversation starters.

Select enough to:

- demonstrate the core purpose,
- expose important supported workflows,
- and reduce entry uncertainty.

Avoid large lists that become a capability catalog.

---

## 41. Starter Lifecycle

Conversation starters are generally generated-assistant metadata.

They should be designed during Builder generation and may be revised when the assistant's architecture changes.

They are not necessarily runtime instructions.

---

## 42. Failure Handling

### 42.1 Starter Implies Unsupported Capability

Remove or rewrite it.

### 42.2 Starter Is Too Broad

Make the task more concrete.

### 42.3 Starter Is Too Specific

Generalize it if the specificity does not materially improve usability.

### 42.4 Starter Duplicates Another

Consolidate.

### 42.5 Starter Becomes Outdated

Revise it when the underlying capability or purpose changes.

### 42.6 User Ignores Starters

Proceed with the user's actual request.

---

## 43. Builder Activation Guidance

The Builder should consider `SM-07` when:

- the assistant has multiple meaningful entry paths,
- users may not know what to ask,
- specialized capabilities benefit from discoverability,
- or a concise first-use orientation materially improves usability.

### Entry Necessity Test

> **Would representative entry guidance materially reduce user uncertainty about how to use this assistant?**

### Capability Exposure Test

> **Are there important supported capabilities that a new user would otherwise be unlikely to discover?**

### Friction Test

> **Would a mandatory opening create more friction than value?**

If yes, use optional starters rather than a fixed sequence.

---

## 44. Validation Requirements

A valid implementation should demonstrate that the assistant can:

1. provide useful representative starters when appropriate,
2. avoid starters when they add no meaningful value,
3. proceed directly when the user already provides a clear request,
4. avoid implying unsupported capabilities,
5. distinguish starters from runtime instructions,
6. distinguish starters from ongoing engagement,
7. expose important specialized capabilities,
8. preserve user freedom to ask other questions,
9. avoid unnecessary onboarding,
10. adapt entry guidance to the assistant's actual purpose,
11. preserve consequential-domain boundaries,
12. preserve political neutrality where applicable,
13. avoid false authority claims,
14. and keep starter content consistent with the actual package architecture.

---

## 45. Suggested Evaluation Cases

### Case A - Specialized Assistant

**Assistant purpose:**

Analyze uploaded business documents.

**Expected starters:**

```text
"Review this report and identify the key risks."

"Compare these two documents."

"Extract the requirements from this proposal."
```

The starters expose distinct supported workflows.

---

### Case B - Clear User Request

**Input:**

"Summarize the attached report in five bullets."

**Expected:**

Begin the requested task rather than forcing a starter-selection process.

---

### Case C - Unsupported Capability

**Assistant capability:**

Can analyze files but cannot modify external systems.

**Bad starter:**

"Upload your spreadsheet and I'll update your database."

**Expected:**

Do not use the starter.

---

### Case D - Multiple Use Cases

**Assistant supports:**

- research,
- document analysis,
- decision support.

**Expected:**

Provide a small representative set covering those major entry paths rather than an exhaustive catalog.

---

### Case E - Persona

**Assistant has an optional thematic persona.**

**Expected:**

The greeting or starter wording may reflect the persona without obscuring the actual task.

---

### Case F - Consequential Domain

**Assistant supports general financial information.**

**Bad starter:**

"Tell me where to invest and I'll tell you exactly what to buy."

**Expected:**

Use wording consistent with actual capability and appropriate boundaries.

---

### Case G - Political Information

**Assistant provides neutral election information.**

**Bad starter:**

"Find out why Candidate A is the best choice."

**Expected:**

Use informational framing such as comparing documented positions or summarizing ballot provisions.

---

## 46. Acceptance Criteria

`SM-07` is architecturally acceptable when:

- entry guidance improves discoverability,
- conversation starters represent actual capabilities,
- clear user requests bypass unnecessary onboarding,
- starters do not become mandatory workflows,
- persona remains optional,
- capability claims remain accurate,
- user agency is preserved,
- and entry guidance remains separate from ongoing interaction behavior.

---

## 47. Minimal Viable Module

The minimum viable implementation requires:

1. entry necessity assessment,
2. representative conversation starters,
3. capability integrity,
4. direct-entry bypass,
5. optional orientation,
6. and starter validation.

Complex onboarding systems should not be introduced unless separately justified.

---

## 48. Platform-Agnostic Requirement

Nothing in this module depends on:

- a specific GPT interface,
- a particular conversation-starter UI,
- a model,
- a chatbot platform,
- a persistent onboarding system,
- or a specific configuration API.

The architecture defines entry behavior independently of implementation technology.

---

## 49. Final Architecture Principle

> **Show users how to begin when that helps, but never confuse an entry point with a mandatory path.**

`SM-07` preserves the useful v1 concepts of Initial User Engagement, User Engagement Strategy, and Conversation Starters while removing the v1 assumption that every assistant requires a rigid, sequential opening.

---

**Artifact Status:** Defined  
**Next Candidate:** `SM-08` - Supplemental User-Guided Preferences and Confirmation