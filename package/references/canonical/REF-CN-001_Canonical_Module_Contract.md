# Canonical Module Contract

**Reference ID:** `REF-CN-001`  
**Architecture Version:** `0.2.0`  
**Status:** Active  
**Authority:** Canonical Structural Reference  
**Owner:** Module Architecture

---

# 1. Purpose

The Canonical Module Contract defines the standard structure used to describe every Governing Module and Supporting Module in the Assistant Package.

It standardizes **how a module is defined**.

It does not define the substantive behavior of any particular module.

---

# 2. Module Definition

A module is a self-contained package component that defines coherent specialized behavior which is included or activated only when relevant to the assistant's purpose or current task.

The module architecture exists to prevent specialized behavior from unnecessarily expanding:

- the Behavioral Kernel;
- the Master Operating Specification;
- unrelated modules.

---

# 3. Module Types

Every module has one of two classifications.

## 3.1 Governing Module

A Governing Module defines substantive specialized behavior that may materially determine how the assistant performs a class of tasks.

Examples:

```text
GM-05 Specialized Methodology Execution
GM-10 Document and File Analysis
GM-11 External Research
GM-12 Multimodal and Image Interpretation
```

## 3.2 Supporting Module

A Supporting Module provides supplemental behavior that improves interaction, presentation, guidance, or task execution without defining the assistant's fundamental specialized operating domain.

Examples:

```text
SM-01 Supplemental User Engagement
SM-04 Supplemental Structured Response and Tone
SM-05 Supplemental Iterative Feedback and Adaptation
SM-07 Supplemental Guided Entry and Conversation Starters
```

---

# 4. Module Contract

Every module should conform to the following conceptual structure:

```text
Module
├── Identity
├── Purpose
├── Classification
├── Scope
├── Activation
├── Status
├── Behavior
├── Dependencies
├── Authority
├── Inputs
├── Outputs
├── Capabilities
├── Limitations
├── Failure Handling
├── Interactions
├── References
├── Validation
└── Acceptance Criteria
```

Not every field requires extensive content.

Optional fields should be included when materially relevant.

---

# 5. Identity

Each module must have a stable identifier and descriptive name.

Example:

```text
ID: GM-11
Name: External Research
```

The identifier must conform to `REF-CN-003`.

---

# 6. Purpose

Purpose should answer:

> Why does this module exist?

A module purpose should identify the specialized outcome or responsibility it supports.

Purpose should not simply restate its filename.

---

# 7. Classification

The module must identify whether it is:

```text
Governing
```

or:

```text
Supporting
```

Classification should reflect architectural responsibility, not historical naming.

---

# 8. Scope

The module should define:

- what behavior it owns;
- what behavior it does not own;
- when it applies;
- when another component should be used instead.

Scope prevents responsibility drift.

---

# 9. Activation

Activation should answer:

> Under what conditions does this module become relevant?

Activation may depend on:

- task type;
- user request;
- assistant purpose;
- available capability;
- source material;
- consequential context;
- explicit user preference;
- materiality.

A module should not be activated merely because it exists.

---

# 10. Availability vs Activation

These concepts must remain distinct.

```text
Available
    ≠
Activated
```

A module may be present in the package without being relevant to the current assistant or task.

Similarly:

```text
Capability available
    ≠
Capability selected
```

---

# 11. Status

A module may have a development status such as:

```text
Planned
Working
Defined
Active
Deprecated
Retired
```

Status describes package lifecycle.

It does not determine whether the module applies to a particular task.

---

# 12. Behavior

The Behavior section defines the substantive specialized behavior owned by the module.

Behavior should be:

- specific enough to guide execution;
- bounded enough to preserve ownership;
- general enough to adapt to context;
- consistent with Kernel invariants;
- consistent with the Master Specification.

Behavior should not unnecessarily reproduce rules already owned by the Kernel or Master Specification.

---

# 13. Dependencies

A module may declare dependencies when another package component is materially required for correct operation.

Typical dependencies include:

```text
kernel
master_spec
REF-CN-001
REF-CN-002
```

Specialized module dependencies should be declared only when necessary.

Dependency declaration does not automatically establish behavioral precedence.

---

# 14. Authority

A module should identify the authority relevant to its specialized behavior when applicable.

Possible authority dimensions include:

```text
Behavioral Authority
Information Authority
Structural Authority
Reference Status
Data Status
```

These dimensions should not be collapsed into one universal authority ranking.

A module may depend on authoritative source material without that source becoming universally authoritative for the entire assistant.

---

# 15. Inputs

Inputs should identify information or material the module may require.

Examples:

- user request;
- user-provided file;
- image;
- external source;
- structured data;
- methodology definition;
- user preference;
- prior interaction state.

Input availability must not be assumed.

---

# 16. Outputs

Outputs should identify what the module contributes to assistant execution.

Examples:

- analyzed information;
- research findings;
- structured comparison;
- methodology execution;
- decision-support framing;
- learning exercise;
- resource recommendations.

Outputs should not imply successful execution when the required capability or input was unavailable.

---

# 17. Capabilities

When a module uses a capability, describe that capability using:

```text
REF-CN-002
Canonical Capability Contract
```

A module should explain:

- why the capability is relevant;
- when it should be used;
- what conditions activate it.

The Capability Contract defines how the capability itself is described.

---

# 18. Limitations

Modules should identify material limitations.

Limitations may include:

- unavailable capability;
- insufficient input;
- source restrictions;
- currentness limitations;
- uncertainty;
- jurisdictional limitations;
- access limitations;
- output limitations.

A module should never conceal a material limitation.

---

# 19. Failure Handling

A module should define what happens when its specialized behavior cannot be completed.

General pattern:

```text
Detect failure
      ↓
Represent failure accurately
      ↓
Preserve known information
      ↓
Use supported fallback when practical
      ↓
Avoid fabricated completion
```

Failure handling should distinguish:

```text
Unavailable
Failed
Incomplete
Unknown
Not applicable
```

when the distinction materially affects the result.

---

# 20. Interactions

A module should identify important interactions with other modules.

Interactions may include:

```text
Composition
Extension
Optional support
Shared input
Shared capability
Sequential use
Conditional activation
```

Modules should not silently assume ownership of another module's responsibilities.

---

# 21. Canonical Ownership

Every substantive behavior should have one canonical owner.

A module should therefore:

- define behavior it owns;
- reference behavior owned elsewhere;
- avoid copying canonical rules unnecessarily;
- avoid creating competing versions of shared rules.

Example:

```text
Kernel
    owns capability reality

GM-11
    specializes research behavior
```

GM-11 should not redefine capability reality as if it were independent behavior.

---

# 22. Relationship to the Kernel

Every module remains subordinate to Kernel invariants.

Modules must not override:

- source fidelity;
- capability reality;
- action honesty;
- evidence integrity;
- claim calibration;
- material uncertainty;
- defined requirements.

Specialized behavior extends the Kernel rather than replacing it.

---

# 23. Relationship to the Master Specification

The Master Specification establishes the general operating baseline.

A module specializes that baseline when necessary.

Conceptually:

```text
Master baseline
        ↓
Specialized module
        ↓
Task-specific application
```

A module should not duplicate the Master Specification simply to make itself appear self-contained.

---

# 24. Governing vs Supporting Decision

Use the following distinction.

### Governing Module

Use when the component:

- defines substantive specialized task behavior;
- materially determines how a class of tasks is executed;
- requires specialized rules, decisions, or safeguards;
- may be necessary for the assistant's intended outcome.

### Supporting Module

Use when the component:

- supplements execution;
- improves interaction or presentation;
- provides optional guidance;
- assists an already-defined task;
- does not independently define the substantive operating domain.

---

# 25. Module Necessity Test

Before creating or retaining a module, ask:

> Does this behavior materially justify an independent architectural component?

A module is justified when separation materially improves one or more of:

- clarity;
- reuse;
- selective activation;
- maintainability;
- behavioral isolation;
- capability composition;
- testing;
- package portability;
- architectural integrity.

If not, the behavior may belong in the Master Specification or another existing component.

---

# 26. Module Duplication Test

Before adding behavior to a module, ask:

1. Does another component already own this behavior?
2. Is this behavior a specialization of an existing canonical rule?
3. Can the module reference the existing rule instead of reproducing it?
4. Would duplication create competing interpretations?

If an existing canonical owner exists, prefer reference and specialization over duplication.

---

# 27. Module Composition

Multiple modules may operate together.

Example:

```text
Kernel
   +
Master Specification
   +
GM-10 Document Analysis
   +
GM-11 External Research
   +
GM-07 Decision Support
   +
SM-04 Structured Response
```

Composition should preserve:

- canonical ownership;
- source provenance;
- capability provenance;
- user requirements;
- uncertainty;
- module boundaries.

---

# 28. Conditional Activation

A module may be:

```text
Available
        ↓
Relevant
        ↓
Activated
        ↓
Executed
```

These are separate states.

The presence of a module in the package does not mean its behavior should influence every interaction.

---

# 29. Platform Agnosticism

The Module Contract must not depend on:

- a specific platform;
- a specific model;
- a specific instruction-field limit;
- a specific retrieval mechanism;
- a specific tool interface;
- a specific connector system;
- a specific user interface.

Modules describe behavior and architectural relationships.

Runtime environments determine actual capability availability.

---

# 30. V1 Building Block Relationship

A V1 Building Block does not automatically become a V2 module.

The migration process is:

```text
V1 Building Block
        ↓
Behavioral Concepts
        ↓
Classification
        ↓
Canonical Ownership
        ↓
Architectural Destination
```

A Building Block may become:

- Kernel behavior;
- Master Specification behavior;
- Governing Module;
- Supporting Module;
- Reference;
- Builder behavior;
- QA criterion;
- consolidated behavior;
- retired behavior.

---

# 31. Migration Integrity

When a V1 concept is represented in a module:

- preserve its meaningful behavior;
- preserve its source lineage;
- document material transformation;
- avoid silently deleting behavior;
- distinguish migration from improvement.

The migration ledger remains the authoritative accounting artifact for V1-to-V2 behavioral lineage.

---

# 32. Validation

A module should be validated for:

### Structural Conformance

Does it conform to this contract?

### Behavioral Ownership

Does it own a coherent responsibility?

### Duplication

Does it unnecessarily duplicate another component?

### Activation

Is there a meaningful reason for it to activate?

### Composition

Can it operate with relevant modules without conflict?

### Capability Integrity

Does it accurately represent required capabilities?

### Failure Integrity

Does it accurately represent limitations and failure?

### Platform Agnosticism

Does it avoid assumptions about a specific implementation platform?

---

# 33. Module Acceptance Checklist

A module conforms when:

- [ ] Identity is defined.
- [ ] Purpose is defined.
- [ ] Classification is defined.
- [ ] Scope is defined.
- [ ] Activation is defined.
- [ ] Status is defined.
- [ ] Behavior is defined.
- [ ] Dependencies are defined when needed.
- [ ] Authority is defined when relevant.
- [ ] Inputs are defined when relevant.
- [ ] Outputs are defined when relevant.
- [ ] Capabilities follow `REF-CN-002`.
- [ ] Limitations are defined when material.
- [ ] Failure handling is defined.
- [ ] Interactions are defined when material.
- [ ] References are identified when relevant.
- [ ] Validation criteria exist.
- [ ] Canonical ownership is clear.
- [ ] Kernel rules are not unnecessarily duplicated.
- [ ] Master Specification rules are not unnecessarily duplicated.
- [ ] The module is materially justified.
- [ ] The module is platform agnostic.

---

# 34. Contract Principle

> **The Module Contract standardizes structure, not substantive behavior.**

A module should be recognizable as a package component without becoming a template that forces unrelated behaviors into the same shape.

---

# 35. Final Principle

> **A module exists because a coherent specialized responsibility deserves an independent architectural boundary.**

If the boundary does not improve clarity, reuse, selective activation, maintainability, testing, or integrity, the behavior probably belongs elsewhere.