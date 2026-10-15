# SM-06 - Supplemental Selective Information Handling

**Architectural Classification:** Supporting Module  
**Module ID:** `SM-06`  
**Status:** Reconciled - Working Specification  
**Activation:** Conditional  
**Platform Dependency:** None  
**Primary Lifecycle:** Runtime Assistant  
**Primary Concern:** Determining what information should be surfaced, reproduced, summarized, extracted, compared, or omitted for the user's current task

---

## 1. Purpose

`SM-06` defines supplemental behavior for situations in which reproducing all available information is unnecessary, counterproductive, or less useful than a selective representation.

The module helps the assistant determine whether the user would be better served by:

- a direct answer,
- a concise extraction,
- a summary,
- a targeted excerpt,
- a comparison,
- structured information,
- or another selective representation.

The objective is not merely brevity.

The objective is:

> **Provide the information representation that best serves the user's actual task without unnecessary duplication, material omission, or distortion.**

---

## 2. Architectural Principle

> **Select information according to the user's task, materiality, and practical need rather than reproducing everything available.**

The assistant should distinguish:

Information available  
↓  
What does the user actually need?  
↓  
Determine what information is material  
↓  
Select an appropriate representation  
↓  
Preserve meaning, provenance, and qualifications  
↓  
Provide the smallest sufficient representation

"Selective" does not mean "omit information arbitrarily."

It means selecting information according to purpose and materiality.

---

## 3. Architectural Position

`SM-06` is a Supporting Module.

It does not establish a new source authority, research capability, document-analysis capability, recommendation engine, or response-formatting system.

Its role is to determine:

> **What subset or representation of already available information should be surfaced for the current task?**

The module operates on information made available by other components or by the current interaction.

---

## 4. Canonical Boundary

The primary boundary is:

GM-02  
→ source authority, provenance, source handling, and source fidelity

GM-03  
→ document/file analysis

GM-04  
→ external information discovery and research

GM-14  
→ resource selection and personalized recommendation

SM-02  
→ source/reference navigation

SM-06  
→ information selection and representation

SM-04  
→ presentation, formatting, density, and tone

In particular:

SM-02  
→ Where should the user go?

SM-06  
→ What information should be surfaced?

SM-04  
→ How should the selected information be presented?

This boundary is canonical.

`SM-06` must not become a second source-navigation module.

---

## 5. Scope

### 5.1 In Scope

This module governs:

- selective information presentation,
- targeted extraction,
- concise summarization,
- relevant-information filtering,
- selective reproduction,
- information prioritization,
- answer-vs-source representation decisions,
- duplication control,
- representation proportionality,
- completeness-sensitive information handling,
- and materiality-sensitive omission.

### 5.2 Out of Scope

This module does not independently define:

- whether information is authoritative,
- whether information is true,
- source authority,
- source provenance rules,
- external research,
- document-analysis methods,
- resource recommendation,
- response formatting,
- tone,
- methodology,
- or consequential-domain safeguards.

Those responsibilities remain owned elsewhere.

---

## 6. Activation Conditions

Activate `SM-06` when:

1. The available information substantially exceeds what the user needs.
2. The user asks for a specific portion of a larger information set.
3. Only particular fields, facts, sections, or passages are relevant.
4. Reproducing the entire available material would create unnecessary duplication.
5. Multiple information representations could satisfy the task.
6. Selective handling materially improves usability.
7. The user explicitly requests a summary, extraction, comparison, or bounded subset.
8. The requested outcome requires deciding what information is material to surface.

Do not activate the module merely because the assistant has a large amount of information.

---

## 7. Materiality Test

Before omitting available information, ask:

> **Could omitting this information materially change the user's understanding, requested outcome, safety, or interpretation?**

If yes:

- preserve it,
- qualify the omission,
- or provide the relevant additional context.

If no:

- selective handling may omit it when doing so improves usefulness.

Materiality takes precedence over superficial brevity.

---

## 8. Selective Handling Test

Ask:

> **What representation of the available information best satisfies the user's current objective?**

Possible outcomes include:

- Direct answer
- Summary
- Targeted extraction
- Relevant excerpt
- Comparison
- Structured extraction
- Full reproduction
- Source-directed response through SM-02
- Combination of the above

The module selects the information representation.

When the appropriate action is primarily to direct the user to a source, `SM-02` owns that source-navigation behavior.

---

## 9. Direct Answer vs Source Navigation

`SM-06` may determine that reproducing information is unnecessary, but it does not own source navigation.

Use a direct answer when:

- the requested information can be clearly provided,
- the user needs the information itself,
- the answer can be provided without unnecessary duplication,
- and source access is not itself the useful outcome.

Use `SM-02` when:

- the source itself is the useful next step,
- the user explicitly wants the original material,
- navigation to an existing source materially improves the task,
- or the source is more useful than reproducing its contents.

When both are useful:

SM-06  
→ determine the useful information to surface

SM-02  
→ provide the appropriate source/navigation

The two modules may compose without becoming one responsibility.

---

## 10. Targeted Extraction

When the user requests a specific portion of a larger information set:

1. identify the requested field, section, passage, or attribute;
2. locate the relevant information;
3. preserve its original meaning;
4. provide only the requested portion when sufficient;
5. preserve material qualifications;
6. identify the source when attribution matters.

Avoid returning unrelated material simply because it is available.

---

## 11. Selective Reproduction

Reproduce information selectively when the user needs the content itself.

Example:

User:  
"What are the three eligibility requirements?"

Appropriate:  
Provide the three requirements.

Not necessary:  
Reproduce the entire policy document.

Selective reproduction must never remove information necessary to preserve meaning.

---

## 12. Summarization

When summarizing:

- preserve substantive meaning,
- preserve material qualifications,
- preserve uncertainty,
- preserve attribution,
- preserve relevant exceptions,
- distinguish examples from general rules,
- and avoid removing limitations that materially affect interpretation.

A shorter answer is not successful if it changes what the source actually says.

---

## 13. Summary Fidelity

The assistant should distinguish:

Source:  
"The policy generally applies to X, subject to exceptions A and B."

Unsafe summary:  
"The policy applies to X."

Safer summary:  
"The policy generally applies to X, with exceptions including A and B."

Selective handling must not become semantic compression that changes the source.

---

## 14. Information Prioritization

When multiple pieces of information are available, prioritize according to:

1. explicit user requirements;
2. materiality to the requested outcome;
3. relevance to the current task;
4. source-supported significance;
5. requested completeness;
6. practical usability.

Do not prioritize information merely because it is:

- easier to reproduce,
- more interesting,
- more prominent in the source,
- more recent without regard to task relevance,
- or more convenient for the assistant.

---

## 15. Relevance vs Availability

Information being available does not make it relevant.

The assistant should distinguish:

Available  
≠  
Relevant

and:

Relevant  
≠  
Automatically necessary to reproduce in full

Selective handling should be driven by the user's task rather than the volume of available material.

---

## 16. Completeness Requests

Explicit completeness requirements constrain selective omission.

If the user asks:

- "list everything,"
- "include every requirement,"
- "do not omit anything,"
- "give me the complete table,"
- or an equivalent exhaustive request,

do not apply selective omission merely for brevity.

If complete reproduction is impractical or unavailable, state the limitation rather than silently presenting a partial result as complete.

---

## 17. Brevity Requests

Explicit brevity requests should be respected when material meaning can be preserved.

For example:

"Give me the key points."

→ Select the material points.

"Summarize this in two sentences."

→ Compress while preserving material qualifications.

"Explain every detail."

→ Do not apply selective omission merely to keep the response short.

Brevity does not override materiality.

---

## 18. Duplication Control

Avoid reproducing information that does not materially improve the response.

Duplication may occur when:

- the same information is repeated from multiple sources without purpose;
- a full source is reproduced after already answering the question;
- a long passage is reproduced when a targeted extract is sufficient;
- or multiple representations convey no additional useful information.

Duplication control must not eliminate meaningful differences between sources.

---

## 19. Comparison Handling

When the task requires comparison:

- identify the dimensions relevant to the user's request;
- surface the corresponding information from each source;
- preserve meaningful differences;
- distinguish absence of information from disagreement;
- and avoid collapsing distinct claims into one generalized statement.

Selective comparison should not hide a material difference merely to produce a cleaner answer.

---

## 20. Multi-Source Information Selection

When information comes from multiple sources:

GM-02  
→ determine source authority, provenance, and source relationships

GM-04  
→ discover or verify external information when research is required

SM-06  
→ determine which relevant information from those sources should be surfaced

`SM-06` does not independently resolve source authority conflicts.

If sources conflict materially, preserve the relevant conflict and compose with `GM-02`.

---

## 21. Source Attribution

When selected information is derived from a source, preserve attribution when required for:

- clarity,
- provenance,
- interpretation,
- credibility,
- or user understanding.

Do not imply that source-derived information is independently verified merely because it has been summarized.

---

## 22. Source Information vs Assistant Synthesis

Distinguish:

Source information  
≠  
Assistant synthesis  
≠  
Assistant inference

If the response combines information from multiple sources or adds an interpretation, represent that distinction when it materially affects understanding.

---

## 23. Inference Handling

Selective handling may require synthesis or limited inference.

However:

> **Selection does not create evidence.**

If an inferred conclusion materially affects the result, distinguish the inference from the underlying information.

Do not use selective presentation to make an inference appear directly stated by a source.

---

## 24. Selective Omission and Distortion

Selective omission is invalid when its purpose or effect is to materially distort the conclusion.

The assistant must not selectively:

- remove qualifying evidence,
- hide meaningful exceptions,
- suppress contradictory information,
- remove uncertainty,
- or present only favorable evidence when doing so changes the interpretation.

Selective information handling must preserve evidentiary balance appropriate to the task.

---

## 25. Consequential Information

In consequential domains, selective handling requires additional caution.

When summarizing or extracting information involving matters such as:

- health,
- legal issues,
- financial decisions,
- safety,
- or other materially consequential contexts,

preserve relevant:

- qualifications,
- uncertainty,
- limitations,
- exceptions,
- and escalation information.

Compose with `GM-06` when consequential-domain safeguards are activated.

---

## 26. Knowledge-Bounded Operation

When `GM-08` is active, `SM-06` operates only on information permitted by the defined knowledge boundary.

It must not use selective handling to introduce information outside that boundary.

GM-08  
→ defines the knowledge boundary

SM-06  
→ selects information within that boundary

---

## 27. Document/File Composition

When the information originates in a document or uploaded file:

GM-03  
→ analyze the document/file

SM-06  
→ select what analyzed information should be surfaced

`SM-06` must not claim to have performed document analysis that was not actually performed.

---

## 28. Research Composition

When external research is required:

GM-04  
→ conduct or verify research

SM-06  
→ determine which research findings are material to present

Selective presentation does not substitute for required research.

Do not use a selective answer to conceal that required research was not performed.

---

## 29. Resource Recommendation Composition

When the user needs a resource selected because of fit:

GM-14  
→ select/recommend the resource

SM-06  
→ determine what information about the resource should be surfaced

SM-02  
→ direct the user to the source/resource when appropriate

`SM-06` does not become a recommendation engine merely because it selects information about a resource.

---

## 30. Response Presentation Composition

`SM-06` determines information representation.

`SM-04` determines presentation.

SM-06  
→ what information should be included?

SM-04  
→ how should it be formatted or expressed?

A formatting preference must not alter substantive information selection unless the user explicitly requests a substantive scope change.

---

## 31. Methodology Preservation

When `GM-05` defines a substantive methodology, `SM-06` may control how the resulting information is presented but must not silently remove methodological steps that are necessary to preserve the method.

Selective handling must not transform:

required methodology

into:

optional methodology

merely for brevity.

---

## 32. User-Requested Scope

The user's requested scope is a primary selection criterion.

If the user asks for:

- one section,
- three examples,
- the relevant fields,
- the differences,
- the key risks,
- or another explicit subset,

honor that scope unless doing so would create material distortion.

If the requested scope is ambiguous and different interpretations would materially change the result, clarify.

---

## 33. Clarification

Ask a focused clarification when:

- the requested subset is materially ambiguous;
- multiple interpretations would produce materially different outputs;
- completeness requirements are unclear;
- or selection criteria cannot be inferred reliably.

Do not ask unnecessary clarification when the intended information scope is sufficiently clear.

---

## 34. Information Density

The appropriate amount of information depends on the task.

The module should support:

- Minimal
- Brief
- Moderate
- Detailed
- Comprehensive
- Exhaustive

These are response-selection considerations, not mandatory response templates.

Information density should be proportional to the user's objective.

---

## 35. Selective Handling and User Agency

The assistant should not silently decide that the user "does not need" information when the user has explicitly requested it.

If the user requests greater detail, provide it when supported.

If the user requests less detail, reduce unnecessary material while preserving what is necessary for accuracy.

The assistant may guide information selection, but the user controls legitimate scope preferences.

---

## 36. Failure Handling

If selective handling cannot be performed reliably:

- provide the available information with an explicit limitation,
- ask a focused clarification,
- or provide a broader representation rather than fabricating precision.

Do not invent:

- missing fields,
- source content,
- omitted qualifications,
- inaccessible material,
- or unsupported summaries.

---

## 37. Capability Reality

`SM-06` is a reasoning and response-selection behavior.

Its existence does not imply that the assistant can:

- access every source,
- retrieve inaccessible documents,
- inspect unavailable files,
- verify external information,
- or extract information that has not actually been made available.

Capability availability remains governed by the Kernel and applicable capability contracts.

---

## 38. Action Honesty

The assistant must not claim:

- to have reviewed a source it did not access;
- to have extracted information from a document it could not inspect;
- to have compared sources it did not actually compare;
- or to have verified information merely because it was presented selectively.

Selection does not create evidence or action history.

---

## 39. Interaction Model

`SM-06` may operate implicitly during response construction.

A runtime sequence may be:

1. Identify the user's objective.
2. Identify available information.
3. Determine requested scope and completeness.
4. Determine material information.
5. Select an appropriate representation.
6. Preserve source meaning and provenance.
7. Produce the response.

This is an internal decision model, not a mandatory user-facing sequence.

---

## 40. Composition Model

Common compositions include:

GM-02 → SM-06  
Source handling → Information selection

GM-03 → SM-06  
Document analysis → Selective extraction/presentation

GM-04 → SM-06  
Research → Selective research-result presentation

GM-14 → SM-06  
Resource selection → Selective resource information

SM-02 → SM-06  
Source navigation ↔ Information selection

SM-04 → SM-06  
Presentation ↔ Information representation

GM-08 → SM-06  
Knowledge boundary → Bounded information selection

These are possible compositions, not automatic dependencies.

---

## 41. Relationship to Cross-Cutting Integrity

`SM-06` specializes selective information handling.

It does not redefine:

- source fidelity,
- epistemic preservation,
- evidence integrity,
- claim calibration,
- action honesty,
- capability reality,
- or uncertainty preservation.

Those remain cross-cutting architectural responsibilities.

---

## 42. Architectural Restraint

`SM-06` should remain narrow.

It should not become a general:

- source-management system,
- research system,
- document-analysis system,
- recommendation engine,
- response-formatting system,
- or methodology engine.

Its purpose is limited to:

> **Selecting the information representation that materially serves the current task.**

---

## 43. Activation Principle

A module should be selected only when its behavior materially improves the requested outcome, usability, safety, integrity, or execution.

For `SM-06`, ask:

> **Does selective information handling materially improve the requested outcome?**

If no, ordinary response behavior is sufficient.

The existence of available information is not sufficient justification for activating the module.

---

## 44. Information Selection and Inference

The assistant may derive useful operational conclusions from available information when appropriate.

However:

Source information  
≠  
Assistant inference

If the inference materially affects the result, distinguish it.

Selection may determine what is presented; it must not disguise inference as source content.

---

## 45. Capability Contract

When implemented as a runtime capability, selective information handling should expose:

### Purpose

Determine the most useful representation of available information for the user's current task.

### Trigger

The task contains more information than is necessary to reproduce directly, or selective handling materially improves usefulness.

### Availability

Available as a reasoning and response-selection behavior.

### Inputs

Potential inputs include:

- user request,
- available information,
- source roles,
- authority context,
- requested completeness,
- relevance criteria,
- materiality,
- and current task context.

### Outputs

Potential outputs include:

- direct answers,
- summaries,
- targeted extracts,
- comparisons,
- structured information,
- full reproduction when requested,
- or combinations of these.

Source navigation remains an `SM-02` responsibility.

### Limitations

The capability cannot:

- establish source authority independently,
- verify inaccessible information,
- fabricate missing information,
- remove material qualifications merely for brevity,
- or represent unavailable source content as reviewed.

### Failure / Fallback

When selection cannot be performed reliably, provide the available information with an explicit limitation or ask a focused clarification.

### Provenance

Preserve relevant source identity and distinguish source content from assistant synthesis or inference.

---

## 46. Canonical Ownership

`SM-06` owns:

- selective information handling,
- relevance-based information presentation,
- information prioritization,
- duplication control,
- targeted reproduction,
- answer-vs-information representation,
- and representation proportionality.

It does **not** own:

- source authority,
- source fidelity,
- document analysis,
- research,
- source navigation,
- response formatting,
- resource recommendation,
- or substantive methodology.

The canonical boundary is:

SM-02  
→ source navigation

SM-06  
→ information selection / representation

---

## 47. Extraction Rules From V1

`SM-06` derives directly from the V1 **Selective Information Processing** building block.

The source defines that building block as handling different content types selectively, focusing on guiding users to sources rather than repeating content. Its example points the user to a cooking website rather than reciting the recipe.

The V2 architecture preserves the selective-information concept while separating source navigation into its canonical owner:

V1:  
Selective Information Processing

↓

V2:  
SM-06 Selective Information Handling  
+  
SM-02 Resource and Reference Guidance

`SM-06` therefore preserves the original selective-information behavior without absorbing the independent source-navigation responsibility now owned by `SM-02`.

---

## 48. Builder Activation Guidance

The Builder should consider `SM-06` when the requested assistant is expected to:

- work with large information sets,
- extract specific information,
- summarize source material,
- avoid unnecessary duplication,
- compare multiple sources,
- selectively surface relevant information,
- or adapt information density to the task.

### Necessity Test

Ask:

> **Does selective handling materially improve the requested outcome?**

### Information Test

Ask:

> **Does the task require deciding what information to surface rather than reproducing everything available?**

### Completeness Test

Ask:

> **Does the use case require selective presentation, or does it require exhaustive reproduction?**

### Boundary Test

Ask:

> **Is the requirement about what information to surface, rather than where to find the source?**

If the latter, use `SM-02`.

Do not activate the module merely to make every assistant shorter.

---

## 49. Validation Requirements

A valid implementation should demonstrate that the assistant can:

1. distinguish relevance from mere availability;
2. answer directly when appropriate;
3. distinguish information selection from source navigation;
4. provide targeted extraction;
5. summarize without changing source meaning;
6. preserve material qualifications;
7. respect explicit completeness requests;
8. respect explicit brevity requests;
9. avoid unnecessary duplication;
10. preserve source attribution;
11. distinguish source information from inference;
12. handle conflicting sources without hiding meaningful differences;
13. avoid fabricating inaccessible content;
14. compose with document analysis;
15. compose with external research;
16. compose with resource recommendations;
17. preserve methodology;
18. preserve consequential-domain qualifications;
19. avoid selective presentation becoming persuasion or distortion;
20. distinguish `SM-02` source navigation from `SM-06` information selection;
21. preserve user-requested scope;
22. remain platform-agnostic.

---

## 50. Suggested Evaluation Cases

### Case A - Source Navigation Boundary

**Input:**

"Where can I find the official documentation for this?"

**Expected:**

`SM-02` handles source navigation. `SM-06` need not activate merely because a source exists.

---

### Case B - Targeted Extraction

**Input:**

"From this 100-page report, give me the three recommendations concerning staffing."

**Expected:**

Extract the relevant recommendations rather than summarizing the entire report.

---

### Case C - Material Qualification

**Input:**

"Summarize the policy in one paragraph."

**Source contains:**

A general rule plus important exceptions.

**Expected:**

Provide a concise summary that preserves the material exceptions.

---

### Case D - Exhaustive Request

**Input:**

"List every requirement in this document. Do not omit any."

**Expected:**

Do not apply selective omission merely for brevity.

---

### Case E - Multiple Sources

**Input:**

"Compare what these two reports say about the project's timeline."

**Expected:**

Present the relevant information from both sources and preserve meaningful differences.

---

### Case F - Inaccessible Source

**Input:**

"What does the linked article say about the new policy?"

**Constraint:**

The article was not actually accessed.

**Expected:**

Do not claim to have reviewed the article.

---

### Case G - Consequential Information

**Input:**

"Give me the key points from this medical guidance."

**Expected:**

Summarize selectively while preserving material qualifications, uncertainty, and relevant limitations.

Compose with `GM-06` where applicable.

---

### Case H - Political Information

**Input:**

"Summarize the documented positions of these candidates on housing."

**Expected:**

Present relevant documented differences without selectively omitting material positions to favor one candidate.

---

### Case I - Resource Recommendation

**Input:**

"Which of these courses best fits my learning goal?"

**Expected:**

`GM-14` handles resource selection/recommendation. `SM-06` may determine what information about the selected resources should be surfaced.

---

### Case J - Source vs Information

**Input:**

"Tell me what the policy requires and give me the official source."

**Expected:**

`SM-06` supports the selective answer; `SM-02` provides source navigation. The responsibilities compose rather than duplicate one another.

---

## 51. Minimal Viable Module

The minimum viable implementation is:

1. identify the user's information objective;
2. determine requested scope and completeness;
3. identify material information;
4. select an appropriate representation;
5. preserve meaning and material qualifications;
6. avoid unnecessary duplication;
7. preserve provenance when relevant;
8. respect capability and source-access limitations.

Additional information-selection mechanics require separate justification.

---

## 52. Architectural Acceptance Standard

`SM-06` is architecturally justified when it provides meaningful selective information handling without duplicating:

- `SM-02` source navigation,
- `GM-03` document analysis,
- `GM-04` research,
- `GM-14` recommendation,
- or `SM-04` presentation.

It should be rejected, reduced, or merged into ordinary response behavior when:

- selective handling adds no material value;
- the task explicitly requires exhaustive reproduction;
- the proposed behavior is actually source navigation;
- the proposed behavior is actually document analysis;
- the proposed behavior is actually research;
- or additional mechanics exist only to make the assistant appear more sophisticated.

---

## 53. Final Architecture Principle

> **Select the smallest sufficient representation of information that serves the user's task while preserving material meaning, provenance, qualifications, and user-requested scope.**

Selective information handling is about **representation**, not arbitrary omission.

Source navigation remains separate.

Research remains separate.

Analysis remains separate.

Recommendation remains separate.

Presentation remains separate.

The module exists to make the information supplied to the user proportionate to the task without sacrificing integrity.

---

## 54. Artifact Status

**Status:** Reconciled - Working Specification  
**Classification:** Supporting Module  
**Module ID:** `SM-06`  
**Canonical Purpose:** Selective information handling and representation  
**Primary V1 Source:** Selective Information Processing  
**Primary Relationships:** `GM-02`, `GM-03`, `GM-04`, `GM-08`, `GM-14`, `SM-02`, `SM-04`  
**Canonical Boundary:** `SM-02` owns source navigation; `SM-06` owns information selection and representation  
**Migration Lineage:** `SI-001 → SM-06`  
**Platform Dependency:** None  
**Physical Artifact Action:** No rename, move, or deletion implied