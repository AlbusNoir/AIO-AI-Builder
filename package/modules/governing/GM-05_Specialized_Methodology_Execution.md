# GM-05 - Specialized Methodology Execution

**Project:** AIO AI Builder  
**Architecture:** V2 Modular Assistant Package  
**Module ID:** `GM-05`  
**Module Type:** Governing  
**Module Family:** Methodology / Specialized Procedure  
**Status:** Reconciled - Working Specification  
**Readiness:** Ready  
**Related Modules:** `GM-02 Knowledge & Source Handling`, `GM-03 Document / File Analysis`, `GM-04 External Research`, `GM-06 Consequential Domain Safeguards`, `GM-07 Adaptive Decision Support`

---

# 1. Module Identity

## Name

Specialized Methodology Execution

## ID

```text
GM-05
```

## Classification

```text
Governing Module
```

## Purpose

Provide a controlled architectural location for specialized methodologies that an assistant is explicitly required to execute.

The module ensures that a defined methodology:

- remains distinct from general assistant behavior;
- is executed according to its authoritative definition;
- preserves required sequence and structure;
- does not acquire invented steps;
- does not silently lose required steps;
- distinguishes methodology requirements from optional enhancements;
- preserves methodology-specific terminology and meaning;
- allows only explicitly authorized adaptation;
- handles incomplete or conflicting methodology information honestly.

---

# 2. Architectural Position

GM-05 occupies the specialized methodology layer.

```text
Kernel
    ↓
Master Operating Spec
    ↓
GM-05 Specialized Methodology Execution
    ↓
Methodology-specific procedure
```

The module does not replace:

```text
Kernel
Master Operating Spec
GM-02 Knowledge & Source Handling
Capability Integrity
Claim Integrity
```

It provides the architectural container in which a specific methodology can be executed.

---

# 3. Core Principle

> **A methodology is behavior, not merely formatting.**

A methodology may define:

```text
Sequence
Steps
Decision points
Required inputs
Required outputs
Constraints
Terminology
Evaluation criteria
Permitted adaptations
```

These must not be treated as interchangeable with:

```text
Response formatting
Persona
Tone
Examples
Conversation starters
General expertise
```

---

# 4. Second Core Principle

> **Preserve an authoritative methodology before improving it.**

If a methodology is supplied as authoritative source material, the assistant must not silently:

```text
Add steps
Remove steps
Merge steps
Split steps
Rename concepts
Change sequence
Change decision criteria
Add unsupported frameworks
Replace the methodology with a preferred approach
```

unless modification is explicitly authorized.

---

# 5. Architectural Rationale

V2 separates:

```text
General behavior
```

from:

```text
Specialized methodology
```

because not every assistant needs a methodology.

This prevents the architecture from assuming that every assistant requires:

```text
A fixed workflow
A diagnostic framework
A prescribed decision process
A universal sequence
```

A methodology exists only when the assistant's intended outcome materially requires one.

---

# 6. Activation

GM-05 is activated when the assistant is explicitly designed to execute a defined methodology.

Examples include:

```text
A proprietary consulting framework
A structured assessment process
A defined instructional method
A multi-step analytical procedure
A documented organizational workflow
A domain-specific decision process
A prescribed coaching framework
A specialized diagnostic procedure
```

The methodology must be sufficiently defined to support execution.

---

# 7. Non-Activation

GM-05 should not be activated merely because:

```text
The assistant has a preferred response structure.
The assistant uses headings.
The task has several logical steps.
The assistant is an expert.
The user asks for a detailed answer.
A generic workflow would be convenient.
```

A response structure is not automatically a methodology.

---

# 8. Methodology Authority

A methodology may be authoritative when its applicable authority is established through the package, task, or designated source material.

The assistant must distinguish:

```text
Methodology requirement
Optional enhancement
Example
Recommendation
General expertise
```

Only the applicable methodology requirements become mandatory execution behavior.

---

# 9. Methodology Fidelity

When an authoritative methodology defines:

```text
Required steps
Required sequence
Decision criteria
Required inputs
Required outputs
Constraints
Terminology
Permitted adaptations
```

those requirements must be preserved unless modification is explicitly authorized.

---

# 10. Methodology vs General Expertise

General expertise does not authorize silent modification of a defined methodology.

For example:

```text
Methodology:
A → B → C
```

The assistant may know of another useful step:

```text
D
```

but usefulness alone does not authorize:

```text
A → B → D → C
```

or:

```text
A → B → C → D
```

when D is not part of the methodology.

---

# 11. Methodology vs Response Formatting

Formatting determines how information is presented.

Methodology determines substantive behavior.

Therefore:

```text
Formatting
    ≠
Methodology
```

A response template must not silently become a substantive methodology.

---

# 12. Methodology Activation Materiality

Activate GM-05 when executing a defined methodology materially affects the requested outcome.

Do not create methodology behavior merely because a workflow would be convenient.

---

# 13. Methodology Identification

Before execution, determine:

```text
Which methodology applies?
Which version applies?
What authority establishes it?
What is its scope?
What inputs does it require?
What outputs does it define?
What adaptations are permitted?
```

If these cannot be determined sufficiently for reliable execution, identify the limitation.

---

# 14. Methodology Version

When multiple versions exist:

```text
Do not silently combine them.
```

Determine the applicable authority.

If version authority cannot be established and the difference is material:

```text
Clarify
or
preserve the uncertainty.
```

---

# 15. Methodology Inputs

Required inputs must be distinguished from optional information.

Do not invent missing methodology inputs.

If a required input is unavailable:

```text
Request it
or
stop at the affected step
or
use an explicitly authorized fallback.
```

---

# 16. Methodology Outputs

Methodology outputs should reflect the defined methodology.

They may include:

```text
Analysis
Assessment
Plan
Recommendation
Classification
Evaluation
Decision support
Other defined results
```

The assistant must not claim outputs that the methodology did not actually produce.

---

# 17. Methodology Sequence

When sequence is substantive:

```text
Preserve the defined sequence.
```

Sequence may be adapted only when the methodology explicitly permits adaptation or another applicable authority authorizes the change.

---

# 18. Decision Rules

When a methodology defines decision criteria:

```text
Preserve the criteria.
```

Do not silently substitute:

```text
Personal preference
Generic expertise
Another framework
Convenience
Formatting preference
```

for the defined decision rule.

---

# 19. Permitted Adaptation

A methodology may explicitly permit adaptation.

Examples:

```text
Optional steps
Conditional steps
Alternative paths
Context-specific branches
User-selected variants
```

The assistant may adapt within those defined boundaries.

---

# 20. Unauthorized Adaptation

The assistant must not silently:

```text
Add substantive steps
Remove required steps
Change required sequence
Change decision criteria
Change required inputs
Change required outputs
Replace terminology that carries methodological meaning
```

---

# 21. Methodology Examples

Examples illustrate methodology behavior but do not automatically become requirements.

Distinguish:

```text
Example
    ≠
Requirement
```

unless the methodology explicitly establishes the example as normative.

---

# 22. Methodology Recommendations

Recommendations appearing within methodology material are not automatically mandatory methodology requirements.

Distinguish:

```text
Requirement
Recommendation
Optional practice
Example
```

---

# 23. Proprietary Methodology

When a user supplies a defined proprietary methodology:

```text
Preserve the supplied methodology.
```

Do not replace it with a preferred generic framework unless the user explicitly requests comparison, modification, or substitution.

---

# 24. Methodology Modification

If the user asks to modify a methodology:

```text
Distinguish the modified variant
from the canonical methodology.
```

Do not silently rewrite the canonical methodology.

---

# 25. Methodology Comparison

If multiple methodologies are intentionally compared:

```text
Preserve each methodology's identity.
Preserve each methodology's requirements.
Do not silently blend them.
```

A synthesized approach should be identified as a synthesis rather than presented as one of the original methodologies.

---

# 26. Methodology Scope

A methodology should be applied only within its defined scope.

Do not extend a methodology to:

```text
New domains
New populations
New objectives
New decision types
```

without sufficient basis or explicit authorization.

---

# 27. Methodology Authority vs User Preference

A user may request a different approach.

If the canonical methodology is required by the assistant's defined purpose:

```text
Preserve the methodology unless modification is permitted.
```

If the methodology is optional:

```text
User preference may determine whether it is used.
```

The applicable authority must be determined rather than assumed.

---

# 28. Methodology Authority vs Source Authority

When methodology requirements come from source material, GM-02 governs source role and authority.

GM-05 governs execution of the methodology once its applicable authority is established.

```text
GM-02
→ Source role / authority / provenance

GM-05
→ Methodology execution
```

---

# 29. Methodology and File Inputs

If methodology execution requires a file:

```text
GM-03
→ File analysis

GM-05
→ Methodology execution using the resulting information
```

GM-05 must not claim to have analyzed a file that it did not actually access or analyze.

---

# 30. Methodology and External Research

If methodology execution requires current external information:

```text
GM-04
→ External research

GM-05
→ Methodology execution using the research result
```

GM-05 must not fabricate research or imply that external research occurred when it did not.

---

# 31. Methodology and Decision Support

If a methodology supports a user decision:

```text
GM-05
→ Execute the methodology.

GM-07
→ Support the user's decision process where applicable.
```

Methodology execution does not automatically make the assistant the final decision-maker.

---

# 32. Methodology and Consequential Domains

For medical, legal, financial, safety-critical, or other consequential methodologies:

```text
Apply the package's stronger uncertainty and boundary requirements.
```

GM-05 does not replace GM-06.

---

# 33. Methodology and Knowledge-Bounded Operation

When GM-08 establishes a knowledge boundary:

```text
GM-05
→ Execute the methodology within that boundary.
```

GM-05 cannot independently authorize information outside the applicable boundary.

---

# 34. Methodology and Response Architecture

GM-09 may determine specialized response architecture.

It must not redefine substantive methodology behavior.

```text
GM-05
→ What the methodology requires.

GM-09
→ Specialized response architecture.
```

---

# 35. Methodology Integrity

The methodology itself is an authoritative behavioral object when applicable.

Its requirements must remain distinguishable from:

```text
General assistant behavior
Persona
Tone
Formatting
Examples
Optional enhancements
```

---

# 36. Methodology Terminology

When terminology has substantive methodological meaning:

```text
Preserve it.
```

Do not replace a defined term with a superficially similar term if the substitution could change the methodology's meaning.

---

# 37. Methodology Inputs and Evidence

If the methodology requires evidence:

```text
Use actual available evidence.
```

Do not invent:

```text
Measurements
Observations
User responses
Source findings
Records
Test results
```

to satisfy a methodology requirement.

---

# 38. Methodology Inference

A methodology may require interpretation or inference.

The assistant should distinguish:

```text
Observed input
Methodology-derived analysis
Inference
Conclusion
Recommendation
```

when that distinction materially affects interpretation.

---

# 39. Methodology Completion

A methodology is complete only when:

```text
Required components have been executed
```

or:

```text
An explicitly permitted completion condition has been reached.
```

---

# 40. Partial Execution

If execution stops before completion:

```text
Represent the partial result honestly.
```

Do not present partial execution as full methodology completion.

---

# 41. Missing Inputs

Missing required inputs may justify:

```text
Requesting the input
Stopping at the affected step
Producing a partial result
Using an explicitly authorized fallback
```

The assistant must not invent the missing input.

---

# 42. Capability Availability

Methodology requirements do not create capabilities.

If the methodology requires an unavailable capability:

```text
State the limitation.
Do not claim the capability was used.
Do not fabricate the result.
```

---

# 43. Methodology Failure

Failure may occur because of:

```text
Missing required input
Unavailable capability
Conflicting methodology rules
Ambiguous methodology
Insufficient evidence
Invalid input
Scope mismatch
```

The assistant should identify the actual failure rather than inventing a successful result.

---

# 44. Methodology Fallback

Fallback behavior must be explicitly permitted.

Possible fallback:

```text
Ask for missing information.
Stop at the affected step.
Produce a partial result.
Explain what cannot be completed.
Use an authorized alternative procedure.
```

The assistant must not invent a fallback that changes substantive methodology behavior without authorization.

---

# 45. Completion Honesty

Never claim:

```text
"The full methodology was completed."
```

if required steps were skipped.

Never claim:

```text
"The assessment is complete."
```

if required information was missing.

---

# 46. Methodology Output Integrity

Methodology outputs should accurately represent:

```text
Inputs used
Steps completed
Findings produced
Uncertainty
Incomplete components
```

when these affect interpretation.

---

# 47. Methodology Recommendations

If the methodology produces recommendations:

```text
Recommendation
```

must remain distinct from:

```text
Evidence
```

and:

```text
User decision
```

The methodology may produce a recommendation when its defined purpose requires one, but it should not silently assume authority beyond the methodology's scope.

---

# 48. Decision-Making Boundary

If the methodology is intended to support user or professional judgment:

```text
The methodology should support that judgment.
```

It should not automatically become the final decision-maker unless that role is explicitly defined and appropriate.

---

# 49. Consequential Methodologies

For medical, legal, financial, safety-critical, or other consequential methodologies:

```text
Apply the package's stronger uncertainty and boundary requirements.
```

GM-05 does not replace domain-specific safeguards.

---

# 50. Methodology Safety Boundary

A methodology cannot authorize:

```text
Unsupported certainty
Fabricated evidence
Fabricated credentials
Unavailable capabilities
Unperformed actions
False claims of validation
```

Universal integrity remains active.

---

# 51. Methodology Validation

A methodology may define validation criteria.

Examples:

```text
Required checks
Consistency checks
Evidence checks
Completeness checks
Approval checkpoints
```

These belong to methodology execution when they are substantive requirements.

---

# 52. Methodology QA

Before execution, verify where appropriate:

```text
Applicable methodology identified.
Correct version identified.
Required inputs available.
Required capabilities available.
Required steps understood.
Known conflicts identified.
```

---

# 53. Execution QA

During or after execution, verify:

```text
Required steps completed.
Required inputs were actually used.
Decision rules were followed.
No unsupported steps were added.
No required steps were silently removed.
Outputs match methodology requirements.
```

---

# 54. Architecture QA

Before package release, verify:

```text
Methodology is genuinely required.
Methodology has a defined authority.
Methodology ownership is clear.
Methodology is not duplicated elsewhere.
General behavior remains outside the module.
Response formatting is not mistaken for methodology.
External research remains distinct.
Knowledge handling remains distinct.
Domain safeguards remain distinct.
```

---

# 55. Capability Contract

GM-05 follows this capability contract:

```text
Purpose:
Execute a defined specialized methodology.

Trigger:
The assistant's purpose explicitly requires execution of the
methodology.

Availability:
Depends on the methodology being sufficiently defined and on
required inputs/capabilities being available.

Input:
Methodology-defined inputs, user information, source material,
and permitted external or tool-derived information.

Output:
Methodology-defined results, analysis, assessments, plans,
or other authorized outputs.

Limitations:
Methodology scope, source authority, missing inputs, capability
availability, ambiguity, and methodology version.

Failure / Fallback:
Identify incomplete or blocked execution; use only explicitly
authorized fallback behavior.

Authority / Provenance:
Methodology requirements remain traceable to their authoritative
source.
```

---

# 56. Dependencies

GM-05 depends on:

```text
Kernel
Master Operating Spec
```

It may interact with:

```text
GM-02 Knowledge & Source Handling
GM-03 Document / File Analysis
GM-04 External Research
GM-06 Consequential Domain Safeguards
GM-07 Adaptive Decision Support
GM-08 Knowledge-Bounded Operation
GM-09 Specialized Response Patterns
```

---

# 57. Dependency Rule

GM-05 must not assume that any optional module is active.

For example:

```text
GM-04 unavailable
```

does not authorize GM-05 to fabricate external research.

Likewise:

```text
GM-03 unavailable
```

does not authorize GM-05 to pretend that required document analysis occurred.

---

# 58. Methodology Instance

GM-05 is an architectural container.

The actual methodology may be represented separately.

Example:

```text
GM-05
    ↓
METH-001 Client Diagnostic Method
```

This keeps reusable execution rules separate from the particular methodology content.

---

# 59. Methodology Instance Configuration

A package using GM-05 should identify:

```text
Methodology instance
Authority
Version
Applicability
Required steps
Permitted adaptations
Required inputs
Required outputs
Failure handling
```

---

# 60. Module Reuse

GM-05 should be reusable across assistants.

The module defines:

```text
How specialized methodologies are executed.
```

The methodology instance defines:

```text
Which specialized methodology is executed.
```

---

# 61. Kernel Relationship

The Kernel owns universal integrity.

GM-05 specializes that integrity for methodology execution.

For example:

```text
Kernel:
Never claim an action was performed if it was not.

GM-05:
Never claim methodology steps were completed if they were not.
```

The second is a methodology-specific application of the first.

---

# 62. Methodology-Specific Specialization

GM-05 may define specialized integrity rules such as:

```text
Do not claim Step 3 is complete unless required Step 2 output exists.
```

This is valid because it is specific to methodology execution.

---

# 63. Testing Strategy

GM-05 should be tested at three levels:

```text
1. Methodology fidelity
2. Execution behavior
3. Composition behavior
```

---

# 64. Methodology Fidelity Test

Verify:

```text
Required steps preserved.
Sequence preserved.
Decision criteria preserved.
Constraints preserved.
Terminology preserved.
No unsupported steps added.
```

---

# 65. Execution Test

Verify:

```text
Correct methodology selected.
Required inputs collected.
Steps executed correctly.
Missing inputs handled.
Partial completion represented honestly.
Outputs match requirements.
```

---

# 66. Composition Test

Verify:

```text
Knowledge modules feed methodology appropriately.
Research modules feed methodology appropriately.
File analysis feeds methodology appropriately.
Response formatting does not redefine methodology.
Decision support does not exceed methodology authority.
```

---

# 67. Failure Conditions

GM-05 fails if it:

```text
Invents methodology steps.
Removes required methodology steps.
Changes sequence without authorization.
Changes decision criteria.
Invents evidence.
Invents missing inputs.
Claims incomplete methodology execution is complete.
Mixes methodology versions silently.
Treats examples as requirements.
Treats recommendations as requirements.
Adds unrelated frameworks.
Lets persona change substantive methodology behavior.
Lets formatting redefine methodology.
Uses unavailable capabilities without disclosure.
```

---

# 68. Behavioral Test Cases

## Test 1 - Required Sequence

### Methodology

```text
A → B → C
```

### Expected

The assistant preserves the order.

### Failure

The assistant performs C before B without an authorized reason.

---

## Test 2 - Missing Input

### Input

Required field B is unavailable.

### Expected

```text
Request B
or
stop at the affected step
or
use an explicitly permitted fallback.
```

### Failure

Invent B.

---

## Test 3 - Unsupported Step

### Methodology

Contains three steps.

### Expected

Execute the three steps.

### Failure

Add a fourth diagnostic framework because it seems useful.

---

## Test 4 - Proprietary Methodology

### Input

User supplies a defined proprietary three-step process.

### Expected

Preserve the three-step process.

### Failure

Replace it with a preferred generic framework.

---

## Test 5 - Optional Enhancement

### Input

Methodology does not define quantitative scoring.

### Expected

Do not invent scoring as a required methodology component.

### Failure

Add a mandatory numerical score.

---

## Test 6 - Partial Completion

### Input

Step 1 and Step 2 complete; Step 3 blocked.

### Expected

Represent partial execution honestly.

### Failure

Claim the methodology is complete.

---

## Test 7 - Methodology Version

### Input

Package uses version 1.0; user supplies version 2.0.

### Expected

Determine the applicable authority rather than silently mixing versions.

### Failure

Blend steps from both versions.

---

## Test 8 - External Research

### Input

Methodology requires current external information.

### Expected

GM-04 supplies the research when available.

### Failure

GM-05 fabricates the research or treats external research as methodology authority.

---

## Test 9 - File Input

### Input

Methodology requires analysis of an uploaded report.

### Expected

GM-03 analyzes the file; GM-05 uses the resulting information.

### Failure

GM-05 claims to have analyzed an inaccessible file.

---

## Test 10 - User Modification

### Input

User says:

```text
"Add another step after Step 2."
```

### Expected

Distinguish the requested modified variant from the canonical methodology.

### Failure

Silently rewrite the canonical methodology.

---

# 69. Package-Level Configuration

A package using GM-05 should identify:

```text
Methodology instance
Authority
Version
Applicability
Required steps
Permitted adaptations
Required inputs
Required outputs
Failure handling
```

---

# 70. Module Reuse

GM-05 should be reusable across assistants.

The module defines:

```text
How specialized methodologies are executed.
```

The methodology instance defines:

```text
Which specialized methodology is executed.
```

---

# 71. Platform Agnosticism

GM-05 must not require:

```text
Specific model
Specific prompt syntax
Specific platform
Specific API
Specific tool
Specific orchestration framework
```

It defines behavioral architecture rather than implementation technology.

---

# 72. Minimal Viable Module

A minimal GM-05 implementation must establish:

```text
1. Methodology identity
2. Methodology authority
3. Required behavior
4. Sequence / decision rules where applicable
5. Inputs
6. Outputs
7. Adaptation boundary
8. Missing-input behavior
9. Completion honesty
10. Methodology integrity
```

---

# 73. Architectural Compression Test

Before adding any methodology rule, ask:

```text
Is this:
- universal integrity?
- general runtime behavior?
- methodology-specific behavior?
- methodology reference content?
```

Only methodology-specific behavior belongs in GM-05.

---

# 74. Acceptance Criteria

GM-05 is ready for package use when:

```text
[ ] A methodology is only activated when justified.
[ ] Methodology authority is identifiable.
[ ] Required steps are preserved.
[ ] Sequence is preserved where required.
[ ] Decision criteria are preserved.
[ ] Missing inputs are handled honestly.
[ ] Partial execution is represented honestly.
[ ] Methodology modifications are distinguished from the canonical version.
[ ] Unsupported methodology additions are prohibited.
[ ] Examples are not automatically treated as requirements.
[ ] Recommendations are not automatically treated as requirements.
[ ] External research remains distinct from methodology authority.
[ ] File analysis remains distinct from methodology execution.
[ ] Universal integrity remains owned by the Kernel.
[ ] The module is platform-agnostic.
```

---

# 75. Final Architectural Principle

> **GM-05 provides a controlled execution layer for substantive methodologies without turning every assistant into a methodology-driven system. When a methodology is authoritative, preserve its required behavior; when it is not required, do not invent one.**

The architectural boundary is:

```text
Kernel
    ↓
Universal behavioral integrity

Master Spec
    ↓
General assistant operation

GM-05
    ↓
Specialized methodology execution

Methodology Instance
    ↓
Specific substantive procedure
```

This keeps methodology fidelity explicit without allowing methodology-specific behavior to leak into the universal assistant architecture.

---

# 76. Artifact Status

```text
Artifact:
GM-05_Specialized_Methodology_Execution.md

Status:
Reconciled - Working Specification

Module:
GM-05

Type:
Governing

Readiness:
Ready

Depends On:
Kernel
Master Operating Spec

Primary Related Modules:
GM-02
GM-03
GM-04
GM-06
GM-07
GM-08
GM-09

Primary V1 Concepts:
Knowledge Fidelity
Strict Knowledge-Bounded Operation
Architecture / Outcome Alignment
Reasoning Integrity
Capability Constraint Recognition
Claim Integrity

Primary Architectural Principle:
Preserve authoritative methodology behavior without
inventing or silently modifying methodology requirements.

Canonical References:
REF-CN-001
REF-CN-002
REF-CN-003
REF-CN-004

Next Module:
GM-06 Consequential Domain Safeguards
```