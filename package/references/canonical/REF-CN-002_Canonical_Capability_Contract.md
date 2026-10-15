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