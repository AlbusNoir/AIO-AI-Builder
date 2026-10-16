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