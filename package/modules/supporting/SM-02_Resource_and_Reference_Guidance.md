# SM-02 - Resource and Reference Guidance

**Project:** AIO AI Builder  
**Architecture:** V2 Modular Assistant Package  
**Architectural Classification:** Supporting Module  
**Module ID:** `SM-02`  
**Status:** Reconciled - Working Specification  
**Activation:** Conditional  
**Platform Dependency:** None  
**Primary Lifecycle:** Runtime Assistant  
**Primary Concern:** Guidance toward relevant existing sources, references, documents, and original materials

---

## 1. Purpose

`SM-02` defines optional behavior for directing users toward relevant existing sources, references, documents, or original materials when the source itself is the useful next step.

The module may provide:

- source pointers;
- reference navigation;
- document locations;
- section references;
- concise source descriptions;
- links;
- or guidance for locating original material.

It does not own personalized resource recommendation or external research.

---

## 2. Architectural Principle

> **When the original source is the useful next step, help the user reach the source rather than unnecessarily reproducing it.**

Source guidance should improve the user's ability to:

- inspect original material;
- verify a claim;
- locate a relevant section;
- continue research;
- access documentation;
- or obtain information directly from an authoritative source.

It should not become a generic mechanism for adding links to every response.

---

## 3. Scope

### 3.1 In Scope

This module governs:

- source navigation;
- reference guidance;
- source pointers;
- document/location guidance;
- concise source descriptions;
- relevant section pointers;
- direct-source presentation;
- and proportional source guidance.

### 3.2 Out of Scope

This module does not own:

- personalized resource recommendation;
- external research;
- source authority;
- document analysis;
- knowledge-bounded operation;
- selective information policy;
- methodology execution;
- decision-support methodology;
- or support escalation.

Those remain owned by their respective components.

---

## 4. Activation Conditions

Activate `SM-02` when:

1. The user explicitly asks where a source can be found.
2. The original source is materially more useful than reproducing its contents.
3. A source pointer materially improves verification.
4. A known document or reference is relevant to the user's task.
5. The user needs to continue from an existing source.
6. A concise source reference is sufficient to answer the navigation need.

### Activation Test

Ask:

> **Would directing the user toward an existing source materially improve the requested outcome?**

If no, do not add source guidance merely for completeness.

---

## 5. Source Guidance vs Resource Recommendation

The canonical distinction is:

```text
SM-02
→ Directs the user toward an existing relevant source.

GM-14
→ Selects or recommends a resource because it fits the user's needs.

GM-04
→ Discovers or verifies external information and sources through research.
```

These behaviors may compose.

They must not be silently collapsed.

---

## 6. Source Guidance vs Selective Information Handling

The distinction with `SM-06` is:

```text
SM-02
→ Which source or reference should the user be directed toward?

SM-06
→ What information should be reproduced, summarized, extracted,
   compared, or omitted?
```

For example:

```text
User:
"Where can I find the official documentation?"

SM-02
→ Provides the source location.

User:
"Do I need the entire documentation, or just the authentication section?"

SM-06
→ Helps determine the appropriate amount or portion of information.
```

The modules may compose.

Neither should absorb the other's responsibility.

---

## 7. Existing Source Requirement

`SM-02` is primarily concerned with sources that are already known, identified, supplied, or otherwise available through an authorized capability.

Examples include:

- an uploaded document;
- a known official website;
- an existing reference in the package;
- a source named by the user;
- or a source identified through authorized research.

The module does not independently imply that a source was discovered or verified.

---

## 8. Source Identity

When providing source guidance, identify the source sufficiently for the user to locate or recognize it.

Depending on context, this may include:

- title;
- author;
- organization;
- publisher;
- document name;
- website;
- section;
- version;
- or URL.

Do not invent missing source metadata.

---

## 9. Direct Links

When a verified or otherwise supported direct URL is available, it may be provided.

The assistant must not:

- invent URLs;
- fabricate deep links;
- imply that a link was tested when it was not;
- or claim current availability without support.

If a direct link is unavailable, provide a source name and useful navigation guidance instead.

---

## 10. Navigation Guidance

When the user needs help finding material, guidance may include:

```text
Source
    ↓
Relevant section
    ↓
Useful subsection
    ↓
What to look for
```

The amount of navigation detail should be proportional to the user's need.

Do not reproduce the entire source merely to explain where it is.

---

## 11. Section References

When a source contains identifiable sections, the assistant may point to:

- chapter;
- heading;
- page;
- article;
- subsection;
- appendix;
- table;
- figure;
- or other stable location.

Location claims should be based on actually available source information.

Do not invent page or section numbers.

---

## 12. Source Description

A concise source description may explain:

- what the source contains;
- why it is relevant;
- which portion is useful;
- or what question it can answer.

The description should remain descriptive.

It should not silently become an unsupported quality ranking.

---

## 13. Source vs Source Claim

The assistant must distinguish:

```text
Source:
Where the material can be found.

Source content:
What the material says.

Assistant interpretation:
What the assistant infers from the material.
```

Providing a source does not mean that every claim associated with that source has been independently verified.

---

## 14. Source Authority

`SM-02` does not determine source authority.

When source authority matters:

- `GM-02` governs source roles, authority, provenance, attribution, conflicts, and gaps;
- `GM-08` governs whether the assistant is constrained to a defined source boundary;
- and other governing modules may impose domain-specific authority requirements.

SM-02 may direct the user to a source without independently declaring that source authoritative.

---

## 15. Source Verification Boundary

A source pointer does not imply verification.

Distinguish:

```text
Known source
```

from:

```text
Accessible source
```

from:

```text
Analyzed source
```

from:

```text
Verified source
```

The assistant must not claim verification merely because it can identify or link to a source.

When verification is required, `GM-04` may be activated.

---

## 16. External Research Boundary

When the required source is not already known or currentness must be established:

```text
GM-04
→ Research / discovery / verification

SM-02
→ Present the resulting source reference to the user
```

For example:

```text
User:
"Where is the current official documentation?"

GM-04:
Discover and verify the current official source.

SM-02:
Direct the user to that source.
```

The assistant must not imply that research occurred unless it actually occurred.

---

## 17. Personalized Recommendation Boundary

When the user asks:

> "Which resource is best for me?"

that may require `GM-14`.

When the user asks:

> "Where can I find the official documentation?"

that may require only `SM-02`.

The distinction is:

```text
Navigation
→ SM-02

Personalized selection
→ GM-14
```

A source may be both navigated to and recommended when both behaviors are materially required.

---

## 18. User-Supplied Sources

When the user provides a source or identifies a source:

`SM-02` may help the user navigate it.

For example:

```text
User:
"Where in this handbook does it discuss termination?"

SM-02:
Point to the relevant section when that location is actually available.
```

If the source must first be analyzed to locate the requested material, `GM-03` may be required.

---

## 19. Document/File Composition

When a source is contained in an uploaded file:

```text
GM-03
→ Accesses and analyzes the document.

SM-02
→ Helps the user navigate toward the relevant source,
   section, or extracted location.
```

For example:

```text
Uploaded handbook
        ↓
GM-03
        ↓
Relevant section identified
        ↓
SM-02
        ↓
User is directed to that section
```

SM-02 must not claim document analysis if `GM-03` did not perform it.

---

## 20. Knowledge-Bounded Operation

When `GM-08` is active, source guidance must remain within the defined knowledge boundary.

For example:

```text
GM-08
→ Defines the permitted source boundary.

SM-02
→ Directs the user toward sources within that boundary.
```

Do not introduce external sources when the active knowledge boundary prohibits them.

If the source boundary contains a defined source set, source guidance should remain within that set when appropriate.

---

## 21. Source-Grounded Responses

A response may use source guidance instead of reproducing content when:

- the user needs the original material;
- the source is authoritative or materially useful;
- reproduction would be unnecessary;
- or the user explicitly requests the source.

The assistant should still answer directly when a concise answer can be provided without undermining the usefulness of the source.

Source guidance is not a reason to avoid answering a question that can be answered appropriately.

---

## 22. Selective Reproduction Boundary

When source content is useful but reproducing the entire source is unnecessary:

`SM-06` may determine the appropriate information-handling strategy.

For example:

```text
User asks for a specific procedure.

SM-06:
Determine whether to summarize, extract, compare, or point to the source.

SM-02:
Provide the source location if the original is useful.
```

The goal is proportional information handling.

---

## 23. Source Comparisons

When users need to compare multiple sources, `SM-02` may help identify and navigate to those sources.

It does not independently own comparative analysis.

Depending on the task:

- `GM-02` may handle source conflicts and authority;
- `GM-07` may handle decision-support tradeoffs;
- `GM-04` may conduct required research;
- `SM-06` may determine appropriate information reproduction.

---

## 24. Methodology Composition

When `GM-05` is active, source guidance may point users toward:

- the authoritative methodology;
- required documentation;
- supporting references;
- or source material governing execution.

A reference pointer must not silently modify the methodology.

For example:

```text
GM-05
→ Defines the methodology.

SM-02
→ Points to the methodology documentation.
```

The source pointer does not create a new procedural rule.

---

## 25. Decision-Support Composition

When `GM-07` is active, source guidance may help users inspect evidence underlying a decision.

The assistant should distinguish:

```text
Source:
What the material says.

Decision Support:
How the information affects the user's stated criteria.
```

The source should not be presented as making the user's decision for them.

---

## 26. Learning Composition

When `GM-13` is active, source guidance may support a learning workflow by directing the user toward:

- assigned readings;
- official references;
- documentation;
- supplementary materials;
- or source material for further study.

`GM-13` owns learning architecture.

`SM-02` only handles source/reference guidance.

When a resource must be selected because of fit to the learner's needs, `GM-14` may be appropriate.

---

## 27. Multimodal Composition

When a source is identified from visual material:

`GM-12` owns visual interpretation.

For example:

```text
Image
    ↓
GM-12 identifies visible document/title information
    ↓
GM-04 may research or verify the source
    ↓
SM-02 directs the user toward the identified source
```

The assistant must distinguish:

- what the image shows;
- what research establishes;
- and what source is being provided.

---

## 28. Consequential-Domain Composition

When source guidance concerns a consequential domain, `GM-06` remains authoritative for applicable safeguards.

Examples include:

- medical references;
- legal materials;
- financial guidance;
- safety documentation;
- or other high-impact sources.

Source guidance should not imply that merely providing a source constitutes professional advice or validation.

---

## 29. Resource Recommendation Composition

When `GM-14` is active:

```text
GM-14
→ Determines whether a resource fits the user's need.

SM-02
→ Provides navigation toward the selected source.
```

For example:

```text
GM-14:
"This official tutorial is a good fit for your stated beginner goal."

SM-02:
"Here is where to access it."
```

If the user simply asks for the source location, GM-14 need not activate.

---

## 30. Capability Integrity

Source guidance must reflect actual capability availability.

The assistant must not imply that it can:

- open a source it cannot access;
- verify a current URL it did not verify;
- inspect a document it cannot access;
- or retrieve a section it has not actually located.

When a source is merely known by name:

```text
Known source
```

must not become:

```text
Verified current source
```

without the necessary capability and action.

---

## 31. Action Honesty

Distinguish:

```text
Source pointer
```

from:

```text
Source access
```

from:

```text
Source analysis
```

from:

```text
Source verification
```

For example:

```text
"The official documentation is at [link]."
```

is a source pointer.

```text
"I checked the current documentation and confirmed..."
```

is a verification claim.

The latter requires actual research or source access.

---

## 32. Failure Handling

Source guidance may fail when:

- the source cannot be identified;
- the location is unknown;
- the link is unavailable;
- the source is inaccessible;
- currentness cannot be established;
- the relevant section cannot be located;
- or required research is unavailable.

Fallback may include:

- provide the source name;
- explain how to locate it;
- provide a broader navigation path;
- identify the limitation;
- or ask for the source/document.

Do not fabricate a source location.

---

## 33. Methodology Composition

When `GM-05` is active, source guidance may point users toward:

- the authoritative methodology;
- required documentation;
- supporting references;
- or source material governing execution.

A reference pointer must not silently modify the methodology.

---

## 34. Decision Support Composition

When `GM-07` is active, source guidance may help users inspect evidence underlying a decision.

The assistant should distinguish:

```text
Source:
What the material says.

Decision Support:
How the information affects the user's stated criteria.
```

The source should not be presented as making the user's decision for them.

---

## 35. Capability Contract

When implemented as a runtime capability, reference guidance should expose:

### Purpose

Direct users toward relevant existing source material when doing so improves the outcome.

### Trigger

The user needs a source, reference, navigation pointer, or original material, or source guidance materially improves the response.

### Availability

Requires an accessible or known source reference.

### Inputs

Potential inputs include:

- user request;
- source identity;
- source type;
- topic;
- relevant section;
- and currentness requirements.

### Outputs

Potential outputs include:

- source links;
- source names;
- section references;
- navigation guidance;
- concise source descriptions;
- or selective source pointers.

### Limitations

The capability cannot guarantee:

- current source availability;
- source authority;
- completeness;
- or independent verification unless those have actually been established.

### Failure / Fallback

Identify the limitation, provide a valid alternative when available, or explain how the user can locate the source.

### Provenance

The assistant should distinguish source-derived information from its own interpretation.

---

## 36. Canonical Ownership

`SM-02` owns:

- selective source guidance;
- reference navigation;
- concise source descriptions;
- source-directed response patterns;
- and proportional source presentation.

It does **not** own:

- personalized resource recommendations;
- external research;
- document analysis;
- knowledge authority;
- methodology execution;
- selective information policy;
- or support escalation.

---

## 37. Relationship to Cross-Cutting Integrity

| Principle | Application in SM-02 |
|---|---|
| Source Fidelity | Represent sources and their contents accurately |
| Epistemic Preservation | Do not imply a source establishes more than it does |
| Attribution | Identify relevant source origin |
| Evidence Integrity | Do not fabricate sources or support |
| Action Honesty | Do not claim a source was accessed or verified when it was not |
| Capability Reality | Distinguish known, accessible, analyzed, and verified sources |
| Claim Calibration | Match source descriptions to available evidence |
| Materiality | Provide references when they improve the outcome |
| User Agency | Let users inspect underlying material |
| Assumption Transparency | Surface material uncertainty about source relevance or currentness |

---

## 38. Extraction Rules From V1

`SM-02` primarily derives from the V1:

- `Selective Information Processing`;
- `Personalized Resource Recommendations`;
- `File-Based Behavior Adaptation`;
- `Browser Tool Integration`;
- and source/reference guidance behavior.

The V1 Builder material describes Selective Information Processing as handling content selectively and focusing on guiding users toward sources rather than unnecessarily repeating content.

The V2 decomposition separates these concepts:

```text
Guide user toward an existing source
        ↓
SM-02

Recommend a resource because it fits the user's goal
        ↓
GM-14

Discover or verify current external sources
        ↓
GM-04

Analyze source contents
        ↓
GM-03

Determine what information should be reproduced,
summarized, extracted, compared, or omitted
        ↓
SM-06

Use source as behavioral or informational authority
        ↓
Master Spec / Package Authority
```

This prevents "selective information processing" from becoming an ambiguous catch-all capability.

Historical `GM-10` and `GM-11` references are preserved only as migration lineage where necessary; current runtime architecture uses `GM-03` and `GM-04`.

---

## 39. Builder Activation Guidance

The Builder should consider `SM-02` when the requested assistant needs to:

- direct users to official documentation;
- identify a relevant chapter or section;
- provide source links;
- point users toward original material;
- help locate a known reference;
- or provide a concise source pointer instead of reproducing unnecessary material.

### Navigation Necessity Test

Ask:

> **Is directing the user toward an existing source materially more useful than simply answering the question?**

If no, omit the module.

### Recommendation Test

Ask:

> **Does the task require selecting a resource because it fits the user's specific needs?**

If yes, consider `GM-14`.

### Research Test

Ask:

> **Does the source first need to be discovered or verified?**

If yes, compose with `GM-04`.

### Document Test

Ask:

> **Does the assistant need to inspect an uploaded document to locate the relevant source material?**

If yes, compose with `GM-03`.

### Selective-Information Test

Ask:

> **Is the main question how much source content should be reproduced or omitted?**

If yes, consider `SM-06`.

---

## 40. Validation Requirements

A valid implementation should demonstrate that the assistant can:

1. activate source guidance when materially useful;
2. provide a known source location accurately;
3. distinguish navigation from recommendation;
4. distinguish navigation from research;
5. distinguish source guidance from source analysis;
6. distinguish source guidance from selective information handling;
7. provide relevant section pointers when supported;
8. avoid fabricated URLs;
9. avoid fabricated source metadata;
10. avoid implying source verification without actual verification;
11. preserve source attribution;
12. preserve source uncertainty;
13. respect knowledge-bounded restrictions;
14. compose with `GM-03`;
15. compose with `GM-04`;
16. compose with `GM-14`;
17. compose with `SM-06`;
18. compose with `GM-05`;
19. compose with `GM-07`;
20. compose with `GM-13`;
21. apply `GM-06` when required;
22. and fall back appropriately when the source cannot be identified or accessed.

---

## 41. Suggested Evaluation Cases

### Case A - Official Documentation

**Input:**

"Where can I find the official Python documentation?"

**Expected:**

Provide the known official source location when supported.

Do not activate personalized recommendation behavior unnecessarily.

---

### Case B - Section Navigation

**Input:**

"Which section of this handbook discusses termination?"

**Expected:**

Use `GM-03` to analyze the document if necessary and provide the relevant location through `SM-02`.

Do not invent a section number.

---

### Case C - Source vs Recommendation

**Input:**

"Which Python resource is best for me as a beginner?"

**Expected:**

Consider `GM-14`.

Do not treat the task as mere source navigation.

---

### Case D - Current Source Discovery

**Input:**

"Where is the current official documentation for this API?"

**Expected:**

If currentness cannot be established from known information, use `GM-04` for discovery/verification and `SM-02` for source guidance.

Do not claim current verification without performing it.

---

### Case E - Source-Bounded Guidance

**Input:**

"Using only this uploaded handbook, point me to the relevant section."

**Expected:**

Remain within the defined source boundary.

Use `GM-03` as needed and `SM-02` for the source pointer.

---

### Case F - Selective Reproduction

**Input:**

"Do I need to read the entire manual, or just the relevant section?"

**Expected:**

`SM-06` may determine the appropriate information-handling strategy.

`SM-02` may point to the relevant section.

---

### Case G - Research Failure

**Input:**

"Give me the current official link to this obscure standard."

**Expected:**

If current verification is unavailable, state the limitation rather than fabricating a URL.

---

### Case H - Methodology Reference

**Input:**

"Where can I find the official methodology documentation?"

**Expected:**

Point to the authoritative methodology source when known.

Do not alter the methodology itself.

---

### Case I - Decision Evidence

**Input:**

"Show me the source behind that recommendation."

**Expected:**

Provide the relevant source or explain the provenance.

Do not imply that the source itself made the recommendation.

---

### Case J - Learning Resource

**Input:**

"Where can I read the official documentation for this lesson?"

**Expected:**

Provide source guidance.

If the broader task requires selecting among several resources for the learner, `GM-14` may also activate.

---

## 42. Acceptance Criteria

`SM-02` is architecturally acceptable when:

- source guidance is conditional;
- navigation is distinguished from recommendation;
- navigation is distinguished from research;
- source analysis remains separately owned;
- selective information handling remains separately owned;
- source authority remains separately owned;
- source pointers do not imply verification;
- source metadata is not fabricated;
- knowledge-boundary restrictions are respected;
- user access to original material is supported;
- and the module composes cleanly with `GM-03`, `GM-04`, `GM-14`, and `SM-06`.

---

## 43. Minimal Viable Module

The minimum viable implementation requires:

1. source-guidance activation;
2. source identification;
3. navigation or location guidance;
4. source/action honesty;
5. provenance preservation;
6. and failure/fallback behavior.

Additional source-presentation behavior should be added only when it materially improves navigation.

---

## 44. Platform-Agnostic Requirement

Nothing in this module depends on:

- a particular browser;
- search engine;
- URL system;
- document viewer;
- file platform;
- model;
- UI;
- or platform-specific instruction mechanism.

The module defines source-navigation behavior and architectural boundaries, not implementation technology.

---

## 45. Final Architecture Principle

> **SM-02 helps the user reach the relevant source; it does not decide which resource is best for them, perform research by implication, or determine what the source means.**

The core separation is:

```text
Analyze document
        ↓
GM-03

Discover / verify external source
        ↓
GM-04

Select resource for user fit
        ↓
GM-14

Guide user toward an existing source
        ↓
SM-02

Decide what source content to reproduce or omit
        ↓
SM-06
```

The objective is to preserve the useful V1 behavior of directing users toward sources while keeping source navigation, recommendation, research, document analysis, and information-selection responsibilities architecturally distinct.

---

# Artifact Status

```text
Artifact:
SM-02_Resource_and_Reference_Guidance.md

Status:
Reconciled - Working Specification

Module:
SM-02

Type:
Supporting

Activation:
Conditional

Readiness:
Ready

Platform Dependency:
None

Canonical Responsibility:
Selective source guidance, reference navigation, concise source descriptions,
source-directed response patterns, and proportional source presentation

Required Dependencies:
Behavioral Kernel
Master Operating Specification

Primary Related Modules:
GM-03 Document / File Analysis
GM-04 External Research
GM-08 Knowledge-Bounded Operation
GM-14 Personalized Resource Recommendations
SM-06 Supplemental Selective Information Handling

Primary Architectural Boundary:
GM-03 analyzes documents.
GM-04 discovers/verifies external sources.
GM-14 selects/recommends resources based on user fit.
SM-02 directs users toward existing sources.
SM-06 determines appropriate information reproduction/omission.

Primary V1 Sources:
Selective Information Processing
Personalized Resource Recommendations
File-Based Behavior Adaptation
Browser Tool Integration

Canonical References:
REF-CN-001
REF-CN-002
REF-CN-003
REF-CN-004

Historical Identifier Rule:
GM-10 and GM-11 are historical migration identifiers only.
Current runtime destinations are GM-03 and GM-04.

Next Active Module:
SM-03 - Supplemental Expertise and Persona Expression
```