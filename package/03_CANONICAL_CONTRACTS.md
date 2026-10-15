# REF-CN-001_Canonical_Module_Contract

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


# REF-CN-002_Canonical_Capability_Contract

# Canonical Capability Contract

**Reference ID:** `REF-CN-002`  
**Architecture Version:** `0.2.0`  
**Status:** Active  
**Authority:** Canonical Structural Reference  
**Owner:** Capability Architecture

---

# 1. Purpose

The Canonical Capability Contract defines the standard structure used to describe capabilities referenced by modules and the Assistant Package.

It standardizes **how a capability is described**.

It does not establish that a capability is actually available in a runtime environment.

---

# 2. Capability Definition

A capability is a mechanism through which an assistant may obtain information, transform information, perform an operation, or produce a result.

Examples include:

- external research;
- file analysis;
- image interpretation;
- structured data processing;
- external actions;
- specialized tool use.

A capability is not:

- a personality;
- a response format;
- a tone;
- a methodology;
- a user preference;
- a desired outcome.

---

# 3. Capability Contract

Every materially relevant capability should be describable through:

```text
Capability
├── Identity
├── Purpose
├── Trigger
├── Availability
├── Input
├── Output
├── Limitations
├── Authority / Provenance
└── Failure / Fallback
```

---

# 4. Identity

Each capability should have a clear descriptive identity.

Example:

```text
Capability: External Web Research
```

The identity should describe the mechanism rather than promise an outcome.

---

# 5. Purpose

Purpose answers:

> Why does this capability exist?

The purpose should connect the capability to a meaningful task or outcome.

A capability should not exist merely because the platform makes it possible.

---

# 6. Trigger

Trigger answers:

> Under what conditions should this capability be considered?

Triggers may include:

- user request;
- current-information requirement;
- material information gap;
- accessible file;
- available image;
- explicit task condition;
- specialized module activation.

A trigger is not itself proof that the capability is available.

---

# 7. Materiality

Capability use should be driven by materiality.

Ask:

> Would using this capability materially improve the requested outcome?

A capability should not be invoked merely because:

- it exists;
- it could be useful in theory;
- it is available;
- it was used previously;
- the task can be made more elaborate with it.

---

# 8. Availability

Availability describes whether the runtime environment actually provides the capability.

Use explicit states when relevant:

```text
Available
Unavailable
Conditional
Future
Unknown
```

These states must remain distinct.

In particular:

```text
Future
    ≠
Available
```

and:

```text
Documented
    ≠
Available
```

---

# 9. Availability vs Activation

These states must not be collapsed:

```text
Capability exists
        ↓
Capability is available
        ↓
Capability is relevant
        ↓
Capability is selected
        ↓
Capability is invoked
        ↓
Capability succeeds or fails
        ↓
Result is produced
```

A capability can be available without being relevant.

A capability can be relevant without being available.

A capability can be invoked without successfully producing a result.

---

# 10. Input

The contract should identify what the capability requires as input.

Input may include:

- user-provided text;
- files;
- images;
- structured data;
- external queries;
- parameters;
- prior results;
- module-defined context.

Distinguish:

```text
Input exists
    ≠
Input is accessible
    ≠
Input is sufficient
```

A capability must not be represented as successfully executed when required input is unavailable or insufficient.

---

# 11. Output

The contract should describe the type of result the capability may produce.

Examples:

- retrieved information;
- extracted text;
- structured data;
- visual observations;
- calculated output;
- external action result.

Output should be represented according to what the capability actually produced.

Do not convert:

```text
Expected output
```

into:

```text
Actual result
```

without execution.

---

# 12. Capability Output Is Not Automatically Evidence

A capability may produce information without establishing that the information is:

- correct;
- authoritative;
- current;
- complete;
- independently verified.

Capability output must therefore retain relevant provenance and uncertainty.

For example:

```text
Search result
    ≠
Verified fact
```

and:

```text
Image observation
    ≠
Confirmed real-world condition
```

---

# 13. Limitations

Every materially relevant capability should identify limitations.

Limitations may include:

- access restrictions;
- unavailable data;
- incomplete input;
- image quality;
- file accessibility;
- source quality;
- currentness;
- jurisdiction;
- execution constraints;
- output uncertainty;
- platform restrictions.

Limitations should be stated when they materially affect the result.

---

# 14. Authority and Provenance

Capability results should preserve provenance when material.

Possible provenance states include:

```text
User-provided
Package-derived
Internal knowledge
External research
Tool-generated
Capability-generated
Inference
Recommendation
```

Provenance should not be silently collapsed.

A capability result may provide information without becoming a governing instruction.

---

# 15. Capability Authority

A capability's existence does not grant it authority over:

- user requirements;
- authoritative source material;
- package instructions;
- methodology;
- user decisions.

Capabilities provide mechanisms.

They do not independently establish behavioral authority.

---

# 16. Failure and Fallback

The contract should define what happens when capability execution:

- fails;
- is unavailable;
- is incomplete;
- produces insufficient output;
- produces uncertain output.

General pattern:

```text
Attempt capability when justified
        ↓
Represent actual execution state
        ↓
Represent actual result
        ↓
Identify material limitation
        ↓
Use supported fallback when practical
```

Never simulate successful execution.

---

# 17. Action Honesty

The assistant must distinguish among:

```text
Capability available
Capability selected
Capability invoked
Capability completed
Result produced
```

The assistant must not claim:

- a search occurred when it did not;
- a file was analyzed when it was inaccessible;
- an image was inspected when it was unavailable;
- an external action was performed when it was not;
- a calculation was executed when it was not;
- a result was obtained when it was not.

---

# 18. Capability Selection

Capability selection should answer three distinct questions.

### Should it be used?

Determined by:

```text
Materiality
+
Requested outcome
```

### Can it be used?

Determined by:

```text
Actual runtime availability
+
Sufficient input
```

### What happened?

Determined by:

```text
Actual execution
+
Actual result
+
Actual provenance
```

These questions must not be conflated.

---

# 19. Capability Composition

Capabilities may be composed.

Example:

```text
External Research
        ↓
Document Analysis
        ↓
Decision Support
        ↓
Structured Response
```

Composition must preserve:

- provenance;
- uncertainty;
- capability state;
- source distinctions;
- failure state.

A downstream capability must not represent an upstream hypothetical result as an actual input.

---

# 20. Capability Dependencies

A module may depend on one or more capabilities.

Example:

```text
GM-11 External Research
    ↓
External Research Capability
```

The module defines:

> when and why the capability should be used.

The Capability Contract defines:

> how the capability is described.

The runtime environment determines:

> whether the capability is actually available.

---

# 21. Capability vs Module

These concepts remain distinct.

### Module

Defines specialized behavior and operating logic.

### Capability

Provides a mechanism that the module may use.

Therefore:

```text
Module
    decides when/why

Capability
    provides mechanism

Runtime environment
    determines availability
```

---

# 22. Capability vs Methodology

A methodology defines a prescribed way of performing substantive work.

A capability provides a mechanism that may assist that work.

For example:

```text
Methodology
    defines required research process

Research capability
    provides external information access
```

The existence of a capability does not define the methodology.

---

# 23. Capability vs Response Format

A response format is not a capability.

Examples:

```text
Use bullet points
Use a table
Use headings
Use concise responses
```

These are presentation behaviors.

They should not be represented as capabilities.

---

# 24. Capability vs Personality

Personality is not a capability.

Examples:

```text
Friendly
Formal
Playful
Professional
Dwarven
Empathetic
```

These describe expression, not mechanisms.

---

# 25. Capability Availability Failure

When a required capability is unavailable:

1. state the material limitation;
2. do not imply the capability is operational;
3. determine whether the task can continue;
4. provide a supported fallback where practical;
5. identify any remaining material requirement.

Do not repeatedly ask the user to enable a capability whose availability is already established.

---

# 26. Conditional Capabilities

Some capabilities may be conditional.

Examples:

```text
Available only with user-provided input
Available only when a specific tool is enabled
Available only for supported file types
Available only under defined permissions
```

Conditional availability should be explicit.

---

# 27. Future Capabilities

Future capability descriptions may be useful for planning.

However:

```text
Future capability
    ≠
Current capability
```

Future capability must never be represented as currently operational.

---

# 28. Unknown Capability State

If availability cannot be established:

```text
Availability = Unknown
```

Do not silently assume availability.

If the task materially depends on the capability, the uncertainty should affect execution.

---

# 29. Capability Integrity

The universal capability integrity rule is:

> **Describe and use capabilities according to actual availability; never claim unavailable or unperformed capability or action, and provide appropriate fallback when practical.**

This rule is a Kernel-level invariant.

This contract provides the structural vocabulary for applying it.

---

# 30. Module Interaction

Modules should reference this contract rather than redefining capability structure independently.

Examples:

```text
GM-10 Document and File Analysis
    → file-analysis capability

GM-11 External Research
    → research capability

GM-12 Multimodal and Image Interpretation
    → visual-analysis capability
```

The modules determine specialized application.

The contract standardizes capability description.

---

# 31. Validation

A capability definition should be checked for:

### Purpose

Is the capability materially justified?

### Availability

Is actual availability distinguished from possibility?

### Trigger

Is there a meaningful reason to invoke it?

### Input

Are required inputs clear?

### Output

Is expected output distinguished from actual result?

### Limitations

Are material limitations represented?

### Provenance

Can the source or execution state be represented accurately?

### Failure

Is unsuccessful execution handled honestly?

---

# 32. Acceptance Checklist

- [ ] Identity is defined.
- [ ] Purpose is defined.
- [ ] Trigger is defined.
- [ ] Availability is defined.
- [ ] Input is defined.
- [ ] Output is defined.
- [ ] Limitations are defined when material.
- [ ] Authority/provenance is defined when material.
- [ ] Failure/fallback behavior is defined.
- [ ] Availability is distinguished from activation.
- [ ] Expected output is distinguished from actual result.
- [ ] Capability output is not automatically treated as evidence.
- [ ] Action honesty is preserved.
- [ ] Platform-specific assumptions are avoided.
- [ ] Capability is not confused with module behavior.
- [ ] Capability is not confused with methodology.
- [ ] Capability is not confused with presentation or persona.

---

# 33. Contract Principle

> **A capability is a mechanism, not a promise.**

Its documentation must distinguish:

- why it exists;
- when it should be used;
- whether it is actually available;
- what it requires;
- what it can produce;
- what limitations apply;
- what actually happened.

---

# 34. Final Principle

> **Never let the description of a capability become evidence that the capability was available, invoked, or successful.**


# REF-CN-003_Canonical_Identifier_Registry

# Canonical Identifier Registry

**Reference ID:** `REF-CN-003`  
**Architecture Version:** `0.2.0`  
**Status:** Active  
**Authority:** Canonical Structural Reference  
**Owner:** Package Architecture

---

# 1. Purpose

The Canonical Identifier Registry defines the identifiers, prefixes, naming conventions, and controlled terminology used throughout the Assistant Package.

Its purpose is to make package artifacts interpretable without requiring undocumented project knowledge.

---

# 2. Identifier Principle

> **No unexplained identifiers.**

Every project-specific identifier, prefix, abbreviation, or controlled vocabulary term that materially affects interpretation should have a defined meaning.

Identifiers should remain stable once they become part of package architecture unless a deliberate migration changes them.

---

# 3. Identifier Families

| Prefix | Meaning |
|---|---|
| `V1-` | V1 source concept |
| `K-` | Behavioral Kernel concept |
| `MS-` | Master Specification concept |
| `GM-` | Governing Module |
| `SM-` | Supporting Module |
| `REF-` | Reference artifact |
| `REF-CN-` | Canonical Reference |
| `B-` | Builder behavior or artifact |
| `QA-` | Quality Assurance / evaluation concept |

---

# 4. Module Identifiers

Governing Modules use:

```text
GM-##
```

Supporting Modules use:

```text
SM-##
```

Examples:

```text
GM-05
GM-10
GM-11

SM-01
SM-04
SM-09
```

The numeric portion identifies the module within the package architecture.

It does not imply:

- priority;
- execution order;
- authority ranking;
- activation frequency.

---

# 5. Canonical Reference Identifiers

Canonical references use:

```text
REF-CN-###
```

Current canonical references:

| Identifier | Artifact |
|---|---|
| `REF-CN-001` | Canonical Module Contract |
| `REF-CN-002` | Canonical Capability Contract |
| `REF-CN-003` | Canonical Identifier Registry |
| `REF-CN-006` | Canonical Package Manifest Schema |

The numeric sequence is an identifier, not a claim that missing numbers represent errors.

---

# 6. V1 Lineage Identifiers

V1 concepts use:

```text
V1-[FAMILY]-###
```

Examples:

```text
V1-KF-001
V1-RI-002
V1-CCR-001
```

These identifiers exist to preserve migration lineage.

A V1 concept may map to:

- one V2 concept;
- multiple V2 concepts;
- a consolidated V2 concept;
- multiple architectural destinations.

---

# 7. V1 Concept Families

Examples of established V1 family identifiers include:

| Family | Meaning |
|---|---|
| `KF` | Knowledge Fidelity |
| `RI` | Reasoning Integrity |
| `CCR` | Capability Constraint Recognition |
| `CI` | Claim Integrity |
| `AR` | Architect |
| `SO` | Specificity and Outcome Alignment |
| `RP` | Role, Persona, and Expertise |
| `CQ` | Communication Sequence |
| `RA` | Response Architecture |
| `KB` | Knowledge-Bounded Operation |
| `KP` | Knowledge Priority |
| `CD` | Capability Design |
| `WR` | Web Research |
| `MF` | Multimodal and File Behavior |
| `SC` | Sensitive / Consequential Domains |
| `DA` | Design Assumptions |
| `FC` | Final Auto Check |
| `DT` | Design Decision Test |
| `QA` | Quality Assurance |
| `FS` | Final Standard |

These are migration identifiers.

They do not automatically determine V2 ownership.

---

# 8. Concept vs Destination

The registry distinguishes:

```text
What is this?
```

from:

```text
Where does it belong?
```

A concept identifier describes the source or conceptual behavior.

An architectural identifier describes its destination.

For example:

```text
V1-KF-001
    ↓
Source Fidelity
    ↓
Kernel ownership
```

The source identifier should not be replaced merely because the behavior moved.

---

# 9. Compound Lineage

When multiple source concepts are consolidated:

```text
V1-KF-001
V1-KF-002
V1-KF-003
V1-KF-004
        ↓
Consolidated Source Fidelity concept
```

The migration ledger should preserve all source identifiers.

When one source concept decomposes:

```text
V1-EXAMPLE-001
        ↓
K-...
MS-...
GM-...
QA-...
```

the ledger should preserve the one-to-many relationship.

---

# 10. Architectural Destination Identifiers

Architectural destinations use their component namespace.

Examples:

```text
K-...
MS-...
GM-...
SM-...
REF-...
B-...
QA-...
```

A destination identifier should not be invented merely to make every sentence traceable.

Use identifiers where they improve:

- lineage;
- ownership;
- navigation;
- validation;
- package integrity;
- cross-reference clarity.

---

# 11. File Naming

File names should generally follow:

```text
[IDENTIFIER]_[Descriptive_Name].md
```

Examples:

```text
REF-CN-001_Canonical_Module_Contract.md
REF-CN-002_Canonical_Capability_Contract.md
GM-11_External_Research.md
SM-04_Supplemental_Structured_Response_and_Tone.md
```

The filename should match the manifest path exactly.

---

# 12. Identifier Stability

Once an identifier is actively referenced by:

- the Manifest;
- another artifact;
- a migration ledger;
- a test;
- a canonical contract;

it should not be changed casually.

If an identifier must change, preserve the old identifier in migration history.

---

# 13. Status Vocabulary

Package artifacts may use:

```text
Planned
Working
Defined
Active
Deprecated
Retired
```

These describe lifecycle state.

They do not describe behavioral authority.

---

# 14. Module Classification Vocabulary

Use:

```text
Governing
Supporting
```

for module classification.

Do not create additional module classes without an architectural reason.

---

# 15. Activation Vocabulary

Use:

```text
Required
Optional
Conditional
```

for package inclusion/activation requirements.

These must remain distinct from execution state.

For example:

```text
Conditional
    ≠
Activated

Available
    ≠
Executing
```

---

# 16. Capability Availability Vocabulary

Use:

```text
Available
Unavailable
Conditional
Future
Unknown
```

These describe capability state.

They must not be used as substitutes for:

- activation;
- execution;
- success;
- result quality.

---

# 17. Authority Vocabulary

Where applicable, distinguish:

```text
Behavioral Authority
Information Authority
Structural Authority
Reference / Example
Data
```

These are authority dimensions, not one universal hierarchy.

---

# 18. Disposition Vocabulary

Migration ledger dispositions use:

```text
Preserved
Compressed
Consolidated
Decomposed
Relocated
Generalized
Specialized
Retired
```

Definitions:

### Preserved

Meaningful behavior remains substantially intact.

### Compressed

Equivalent behavior is expressed more compactly without changing intended behavior.

### Consolidated

Multiple overlapping concepts are combined under one canonical concept.

### Decomposed

One source concept is separated into multiple distinct concepts.

### Relocated

Behavior is moved to a different architectural destination.

### Generalized

A source-specific behavior is transformed into a broader reusable principle.

### Specialized

A general behavior is given a narrower domain-specific implementation.

### Retired

The behavior is intentionally removed with documented rationale.

---

# 19. Controlled Architectural Terms

### Behavioral Kernel

The smallest always-on behavioral control layer.

### Master Operating Specification

The general runtime operating baseline between the Kernel and specialized modules.

### Governing Module

A module defining substantive specialized behavior.

### Supporting Module

A module providing supplemental behavior.

### Reference

Material used to define, support, illustrate, or provide information without automatically becoming runtime instruction.

### Capability

A mechanism that may be available to the runtime assistant.

### Manifest

The machine-readable package map.

### Canonical Owner

The single architectural component responsible for defining a substantive behavior.

### Building Block

A V1 source/design primitive from which behavioral concepts may be extracted.

### Architectural Component

The V2 destination selected for an extracted concept.

---

# 20. Manifest Identifiers

The Manifest should use stable identifiers for:

- package;
- modules;
- canonical references;
- other declared package artifacts.

Manifest identifiers must correspond to actual package paths.

---

# 21. Identifier Integrity

An identifier is invalid when:

- it is used inconsistently;
- it refers to multiple unrelated concepts;
- it conflicts with another canonical identifier;
- its meaning is undocumented;
- its manifest path does not exist;
- its artifact name does not match its declared identity.

---

# 22. Validation

Before package release, verify:

- every declared identifier is unique within its namespace;
- every manifest identifier maps to the intended artifact;
- every canonical reference has a stable ID;
- every module has the correct GM/SM classification;
- every referenced identifier exists;
- deprecated identifiers are documented;
- renamed identifiers preserve migration lineage.

---

# 23. Final Principle

> **Identifiers exist to preserve meaning, ownership, lineage, and package integrity-not to create unnecessary bureaucracy.**


# REF-CN-004_Canonical_Package_Manifest_Schema

# Canonical Package Manifest Schema

**Reference ID:** `REF-CN-004`  
**Architecture Version:** `0.2.0`  
**Status:** Active  
**Authority:** Canonical Structural Reference  
**Owner:** Package Architecture

---

# 1. Purpose

The Package Manifest is the machine-readable map of the Assistant Package.

It describes:

- package identity;
- bootstrap;
- Kernel;
- Master Specification;
- modules;
- references;
- package metadata.

It does not become the behavioral specification itself.

---

# 2. Core Principle

> **The Manifest is the package map: complete enough to describe the package, small enough to avoid becoming the package itself.**

---

# 3. Conceptual Schema

```text
Manifest
├── schema_version
├── package
├── bootstrap
├── kernel
├── master_spec
├── modules
├── references
└── metadata
```

---

# 4. Schema Version

`schema_version` identifies the structure of the Manifest itself.

Example:

```json
"schema_version": "1.0"
```

This is distinct from the Assistant Package version.

---

# 5. Package

The `package` object identifies the package.

Required conceptual fields:

```json
{
  "id": "...",
  "name": "...",
  "version": "...",
  "status": "...",
  "description": "..."
}
```

### `id`

Stable package identifier.

### `name`

Human-readable package name.

### `version`

Package architecture/version identifier.

### `status`

Package lifecycle state.

### `description`

Concise description of package purpose.

---

# 6. Bootstrap

The `bootstrap` object identifies the platform-facing bootstrap file.

Example:

```json
{
  "path": "PASTE_THIS_INTO_THE_GPT.txt",
  "required": true,
  "purpose": "Minimal platform-facing bootstrap containing the Behavioral Kernel."
}
```

The bootstrap should remain intentionally small.

---

# 7. Kernel

The `kernel` object identifies where the Behavioral Kernel is represented.

In the current architecture the Kernel is embedded in:

```text
PASTE_THIS_INTO_THE_GPT.txt
```

Example:

```json
{
  "path": "PASTE_THIS_INTO_THE_GPT.txt",
  "required": true,
  "embedded": true,
  "purpose": "Always-on behavioral invariants."
}
```

The Manifest should not require a separate Kernel file unless the architecture deliberately changes.

---

# 8. Master Specification

The `master_spec` object identifies the general runtime specification.

Example:

```json
{
  "path": "02_MASTER_OPERATING_SPEC.md",
  "required": true,
  "version": "working",
  "purpose": "General runtime operating baseline."
}
```

---

# 9. Modules

Modules are grouped by classification:

```text
modules
├── governing
└── supporting
```

Each module entry should identify:

```json
{
  "id": "GM-11",
  "path": "modules/governing/GM-11_External_Research.md",
  "name": "External Research",
  "type": "governing",
  "required": false,
  "activation": "conditional",
  "status": "defined",
  "dependencies": []
}
```

---

# 10. Module Fields

### `id`

Canonical module identifier.

### `path`

Exact package-relative file path.

### `name`

Human-readable module name.

### `type`

Either:

```text
governing
supporting
```

### `required`

Whether the module is structurally required in every package instance.

### `activation`

How the module becomes applicable.

Typical value:

```text
conditional
```

### `status`

Module lifecycle state.

### `dependencies`

Declared package dependencies when materially required.

---

# 11. Required vs Conditional

These concepts are distinct.

### Required

The artifact is structurally required for package operation.

### Optional

The artifact may be present without being required.

### Conditional

The artifact becomes relevant when defined conditions apply.

A module can therefore be:

```text
required = false
activation = conditional
```

without contradiction.

---

# 12. Availability vs Activation

The Manifest describes package structure.

It does not imply that every declared module is active during every task.

Therefore:

```text
Declared
    ≠
Available
    ≠
Relevant
    ≠
Activated
    ≠
Executing
```

---

# 13. References

References are grouped by role.

Current conceptual structure:

```text
references
├── canonical
├── examples
└── templates
```

Each reference entry should identify:

```json
{
  "id": "REF-CN-001",
  "path": "references/canonical/REF-CN-001_Canonical_Module_Contract.md",
  "role": "canonical",
  "required": true,
  "status": "active"
}
```

---

# 14. Reference Roles

Supported conceptual roles include:

```text
canonical
example
template
supporting
data
```

Role describes how the artifact participates in the package.

It does not automatically establish universal behavioral authority.

---

# 15. Authority Dimensions

Package artifacts may have different authority dimensions:

```text
Behavioral Authority
Information Authority
Structural Authority
Reference / Example Status
Data Status
```

The Manifest should describe package structure without collapsing these dimensions into one simplistic authority ranking.

---

# 16. Undeclared Artifacts

An artifact that is not declared in the Manifest does not automatically become governing package instruction.

Its status should be determined through package architecture and authority rules.

This prevents accidental instruction injection through unrelated files.

---

# 17. Missing Artifacts

If a Manifest-declared artifact is missing:

1. identify the missing artifact;
2. do not invent its contents;
3. determine whether the missing artifact is required;
4. determine whether safe operation remains possible;
5. proceed only within supported boundaries.

A missing reference must not be silently replaced with invented material.

---

# 18. Dependency Integrity

Every declared dependency should:

- exist;
- use the correct identifier;
- point to an actual package component;
- be materially justified.

Circular dependencies should be identified during package validation.

---

# 19. Path Integrity

Every declared path must be:

- package-relative;
- exact;
- consistent with filesystem naming;
- associated with the declared identifier.

Example:

```text
Manifest:
GM-11
↓
modules/governing/GM-11_External_Research.md
```

The physical artifact must match.

---

# 20. Structural vs Behavioral Completeness

A Manifest can be structurally complete while the package is behaviorally incomplete.

### Structural completeness

All declared:

- files;
- identifiers;
- paths;
- classifications;
- dependencies

are accounted for.

### Behavioral completeness

The package has been validated to provide the intended behavior.

Both must be evaluated separately.

---

# 21. Manifest Validation

Validate:

### Schema

Does the Manifest conform to this schema?

### Package

Are package identity and version coherent?

### Bootstrap

Does the declared bootstrap exist?

### Kernel

Is the Kernel correctly represented?

### Master Specification

Does the declared Master Specification exist?

### Modules

Do all declared modules exist and have correct classification?

### References

Do declared references exist?

### Dependencies

Do dependencies resolve?

### Paths

Do paths match actual artifacts?

### Identifiers

Do identifiers conform to `REF-CN-003`?

---

# 22. Package Architecture

The intended generated package is:

```text
Assistant Package/
├── PASTE_THIS_INTO_THE_GPT.txt
├── 01_MANIFEST.json
├── 02_MASTER_OPERATING_SPEC.md
├── modules/
│   ├── governing/
│   └── supporting/
└── references/
    ├── canonical/
    ├── examples/
    └── templates/
```

This structure is an architectural target.

The development repository may contain additional artifacts that do not belong in the generated runtime package.

---

# 23. Development Repository vs Generated Package

The development repository may contain:

- migration ledgers;
- architecture maps;
- QA artifacts;
- tests;
- automation;
- source material;
- development documentation;
- changelogs.

These should not automatically be copied into the generated Assistant Package.

The Manifest describes the runtime package, not the entire development repository.

---

# 24. Manifest Authority

The Manifest is authoritative for:

- package structure;
- declared artifact identity;
- package paths;
- module classification;
- package metadata.

The Manifest does not override:

- Kernel behavioral invariants;
- substantive module behavior;
- canonical source authority;
- user requirements.

---

# 25. Package Versioning

Package versioning should describe the package as a whole.

Example:

```text
0.2.0
```

Component versions may evolve independently where necessary.

A package release should verify that component references remain compatible.

---

# 26. Platform Agnosticism

The Manifest must not depend on:

- a specific AI platform;
- a specific model;
- a specific instruction-field limit;
- a specific retrieval implementation;
- a specific tool interface.

It describes package architecture, not platform mechanics.

---

# 27. Acceptance Checklist

- [ ] Schema version exists.
- [ ] Package identity exists.
- [ ] Bootstrap is declared.
- [ ] Kernel representation is declared.
- [ ] Master Specification is declared.
- [ ] Governing modules are declared.
- [ ] Supporting modules are declared.
- [ ] Canonical references are declared.
- [ ] Paths are package-relative.
- [ ] Identifiers conform to `REF-CN-003`.
- [ ] Required/optional/conditional states are explicit.
- [ ] Dependencies resolve.
- [ ] Missing-artifact handling is defined.
- [ ] Structural and behavioral completeness remain distinct.
- [ ] Development artifacts are not implicitly included.
- [ ] Platform-specific assumptions are avoided.

---

# 28. Final Principle

> **The Manifest describes what the package is; it does not become everything the package knows or does.**

