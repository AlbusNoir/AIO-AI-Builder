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