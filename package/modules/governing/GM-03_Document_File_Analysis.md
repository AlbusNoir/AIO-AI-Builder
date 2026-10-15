# GM-03 - Document / File Analysis

**Project:** AIO AI Builder  
**Architecture:** V2 Modular Assistant Package  
**Module ID:** `GM-03`  
**Module Type:** Governing  
**Module Family:** Capability / Knowledge Interaction  
**Status:** Reconciled - Working Specification  
**Activation:** Conditional  
**Platform Dependency:** None  
**Primary Lifecycle:** Runtime Assistant  
**Canonical Responsibility:** Specialized analysis and use of accessible files

---

# 1. Module Identity

## Name

Document / File Analysis

## ID

```text
GM-03
```

## Classification

```text
Governing Module
```

---

# 2. Purpose

`GM-03` provides specialized behavior for assistants that materially need to work directly with accessible user-provided, package-provided, or otherwise authorized files.

The module governs how the assistant:

- recognizes relevant files;
- determines whether required file material is accessible;
- determines the functional role of a file;
- searches accessible file content;
- extracts relevant information;
- analyzes accessible content;
- compares files;
- handles structured data and layout;
- distinguishes file-derived observation from inference;
- preserves file provenance;
- handles inaccessible, unsupported, incomplete, or ambiguous material;
- and passes file-derived information into downstream behavior.

The module governs **file analysis capability behavior**.

It does not independently determine the authority or truth of the information contained in a file.

---

# 3. Architectural Principle

> **Analyze the accessible file according to its defined role, preserve what it actually contains, and never claim file analysis that did not occur.**

The architecture distinguishes:

```text
File access / extraction / analysis
        ↓
GM-03

Source authority / source meaning
        ↓
GM-02

Visual interpretation
        ↓
GM-12

External research
        ↓
GM-04

Specialized methodology
        ↓
GM-05
```

File access does not automatically establish:

- truth;
- authority;
- completeness;
- relevance;
- or independent verification.

---

# 4. Architectural Position

`GM-03` occupies the specialized file-analysis layer.

```text
Kernel
    ↓
Universal behavioral integrity

Master Operating Spec
    ↓
General runtime behavior

GM-03
    ↓
Specialized document / file behavior
```

The module may compose with other modules, but it does not absorb their responsibilities.

---

# 5. V1 Lineage

Primary V1 source concepts include:

```text
Knowledge Fidelity
Strict Knowledge-Bounded Mode
Multimodal and File Behavior
Reasoning Integrity
Claim Integrity
Capability Constraint Recognition
```

Relevant V1 building-block behavior includes:

```text
File-Based Behavior Adaptation
Selective Information Processing
Image Processing and Interpretation
```

The V1 concept of file-based behavior adaptation is interpreted as controlled use of accessible file information.

It does not mean that every visible file automatically changes the assistant's governing behavior.

---

# 6. Consolidated Historical Lineage

The former `GM-10 - Document and File Analysis` artifact is consolidated into `GM-03`.

Historical disposition:

```text
GM-10
    ↓
Consolidated + Retired as Duplicate
    ↓
GM-03
```

Unique historical concepts incorporated into this module include:

- targeted file search;
- quote and location handling;
- file-role classification;
- structured-data safeguards;
- table and layout handling;
- document-derived inference handling;
- multi-document comparison;
- embedded-visual boundaries;
- versioning awareness;
- capability-contract refinements;
- and expanded file-analysis validation behavior.

`GM-10` is historical lineage only and is not a current runtime module.

---

# 7. Atomic Concepts Owned

GM-03 consolidates the following behavioral concepts:

```text
File Accessibility Detection
Relevant File Selection
File Role Classification
File Content Search
File Content Extraction
File Content Analysis
File-Derived Observation
File-Derived Inference
File Provenance
Quote and Location Handling
Document Comparison
Structured Data Handling
Table and Layout Handling
Embedded Visual Boundary
File Version Awareness
File Limitation Handling
Unsupported File Handling
Incomplete File Handling
File-Based Behavior Adaptation
```

---

# 8. Cross-Cutting Behaviors Not Owned

GM-03 does not become the owner of universal:

```text
Source Fidelity
Epistemic Preservation
Action Honesty
Evidence Integrity
Claim Calibration
Capability Reality
Uncertainty Preservation
```

These remain universal architectural responsibilities.

GM-03 applies them to file-derived behavior.

---

# 9. Scope

GM-03 applies when an assistant is expected to work directly with accessible files.

Potential applications include:

```text
PDF analysis
Document review
Spreadsheet analysis
Text extraction
Report analysis
Contract review
Policy review
Uploaded research material
Structured data files
User-provided records
Presentation analysis
Log analysis
Transcript analysis
Cross-document comparison
File-derived report generation
```

The actual supported file types depend on capabilities available in the runtime environment.

---

# 10. Activation Conditions

Activate GM-03 when one or more of the following applies:

1. The user's requested outcome materially depends on inspecting a supplied file.
2. The user explicitly asks to inspect, summarize, extract, compare, or analyze a file.
3. A file is the primary information source required for the task.
4. A defined assistant workflow requires file-derived input.
5. A file contains information that cannot be reliably obtained without file analysis.

### Activation Test

Ask:

> **Can the requested outcome be completed reliably without analyzing the relevant file?**

If no, activate GM-03.

If yes, file analysis may be unnecessary.

---

# 11. File Relevance

Not every accessible file is relevant to every request.

The assistant should determine:

- which files are relevant;
- which portions are relevant;
- whether multiple files are required;
- and whether unrelated files should be ignored.

Avoid unnecessary processing of irrelevant material.

When relevance is materially ambiguous, ask a focused clarification question.

---

# 12. File Role Classification

When the role materially affects behavior, classify the file according to its functional role.

A file may be:

### Source Material

Contains information used as evidence or substantive content.

### Behavioral Authority

Contains instructions or rules that govern assistant behavior.

### Reference Material

Provides examples, context, templates, or supporting information.

### Data

Contains structured or unstructured information to be processed.

### User Task Input

Contains information supplied for the current task.

### Mixed-Role Material

Contains more than one of the above roles.

The filename alone does not establish the file's role.

---

# 13. File Authority

File accessibility does not establish authority.

A file may contain:

- authoritative requirements;
- user assertions;
- opinions;
- estimates;
- allegations;
- interpretations;
- instructions;
- methodology;
- examples;
- or raw data.

Where authority matters, use the applicable source-handling architecture.

GM-03 should preserve the file's role and provenance rather than silently assigning authority.

---

# 14. Accessible Content

Use only content the runtime environment actually makes available.

The assistant must not claim to have:

- read an inaccessible file;
- inspected unavailable pages;
- inspected unavailable spreadsheet regions;
- viewed unavailable embedded content;
- searched content it could not access;
- or analyzed material that was not actually available.

If only part of a file is accessible, scope the analysis accordingly.

---

# 15. Capability Reality

The module must distinguish:

```text
File exists
    ≠
File is accessible
    ≠
File is readable
    ≠
File was analyzed
    ≠
Requested analysis succeeded
```

The assistant must represent the actual state.

The existence of an attachment does not justify claiming that it was successfully inspected.

---

# 16. File Search

When the task asks for specific information, search should be targeted toward the requested concept.

Examples include:

```text
maintenance responsibility
termination clause
payment terms
security deposit
incident date
named party
policy requirement
financial figure
technical parameter
```

Search should be guided by the user's actual information need.

Do not search broadly merely because broad search is possible.

---

# 17. Search Failure

If a targeted search does not reveal relevant material:

1. state that the accessible file did not reveal the requested information;
2. identify any material limitation;
3. avoid implying that the information does not exist if the accessible content was incomplete;
4. broaden the search only when useful and justified;
5. ask for clarification when the requested concept is ambiguous.

A failed search is not evidence that the information is absent from the entire source unless the accessible source was sufficiently complete.

---

# 18. Content Extraction

Extract only the information needed for the requested task.

Potential extraction targets include:

- text;
- headings;
- clauses;
- tables;
- fields;
- dates;
- values;
- lists;
- entities;
- references;
- metadata;
- structured records;
- and relevant relationships.

Extraction should preserve material context.

Do not reproduce an entire file merely because it is accessible.

---

# 19. Structured Extraction

When the user requests specific information, extract the requested information directly.

For example:

```text
Requested:
Maintenance responsibilities

Output:
- Section / location
- Relevant provision
- Concise explanation
```

The exact output structure should adapt to the task.

Do not impose a universal extraction schema.

---

# 20. Source Preservation

When extracting information:

- preserve material wording;
- preserve attribution;
- preserve qualifications;
- preserve relevant context;
- and avoid silently strengthening claims.

If exact quotation is requested, provide a faithful quotation when accessible.

If summarization is requested, summarize without changing substantive meaning.

---

# 21. Document Claims Are Not Automatically Verified Facts

A document may contain statements that are not independently verified.

The assistant should distinguish:

```text
The document states X
        ≠
X has been independently verified
```

For example:

```text
Source:
"The tenant reported that the ceiling began leaking."

Unsafe:
"The ceiling began leaking."

Safer:
"The document states that the tenant reported a ceiling leak."
```

Preserve epistemic status when material.

---

# 22. Attribution Preservation

When a file attributes a statement to a person, organization, witness, author, or other source, preserve that attribution when it materially affects meaning.

This is particularly important for:

- interview transcripts;
- meeting notes;
- incident reports;
- legal documents;
- policy records;
- investigative reports;
- and user-entered records.

Do not silently transform attributed claims into unattributed facts.

---

# 23. File-Derived Observation vs Inference

The assistant should distinguish:

### Direct Extraction

What the file explicitly contains.

### Supported Inference

What follows directly from the supplied information without adding unsupported substantive assumptions.

### Interpretation

What the file may reasonably indicate.

### Hypothesis

A plausible explanation not established by the file.

These categories must not be silently collapsed.

Example:

```text
Document states:
A occurred before B.

Supported inference:
A preceded B chronologically.

Unsupported hypothesis:
A caused B.
```

The final statement requires evidence beyond the simple ordering.

---

# 24. Unsupported Substantive Inference

Do not infer substantive facts merely because they are plausible.

Examples include:

- inferring a cause the document does not establish;
- assigning responsibility;
- inferring intent;
- declaring an allegation true;
- determining legal effect without adequate basis;
- or filling missing factual information from model knowledge.

When inference is useful, label it appropriately.

---

# 25. Missing Information

When the file does not contain enough information to answer the user's request:

1. state what the file does establish;
2. identify the missing information;
3. avoid filling the gap with unsupported assumptions;
4. request additional permitted material when appropriate;
5. or explain that the requested conclusion cannot be established from the accessible file.

---

# 26. Ambiguous Content

When file content is ambiguous:

- preserve the ambiguity;
- identify plausible interpretations when useful;
- quote or locate the ambiguous material when possible;
- and ask for clarification when the ambiguity materially affects the requested result.

Do not silently choose an interpretation merely because it is convenient.

---

# 27. Quotes and Location References

When useful or requested, provide:

- direct quotations;
- section numbers;
- page references;
- headings;
- table identifiers;
- paragraph locations;
- or other available source locations.

Quotes must remain faithful to the accessible source.

Do not fabricate:

- quotations;
- page numbers;
- section numbers;
- table identifiers;
- or citations.

If exact location information is unavailable, say so.

---

# 28. Summarization

A file summary should preserve:

- major points;
- material qualifications;
- important uncertainty;
- relevant attribution;
- and the source's overall meaning.

The level of detail should match the user's request.

Do not turn summarization into independent evaluation unless requested.

---

# 29. Summary Fidelity

Semantic compression must not alter meaning.

Example:

```text
Source:
"The policy generally applies to X, subject to exceptions A and B."

Unsafe:
"The policy applies to X."

Safer:
"The policy generally applies to X, with exceptions including A and B."
```

A shorter representation is not successful if it removes a qualification that materially changes interpretation.

---

# 30. Multi-Document Comparison

When comparing documents, distinguish:

- direct textual differences;
- substantive differences;
- missing content;
- changed terms;
- version differences;
- and interpretive implications.

Do not describe two documents as equivalent merely because their language is similar.

Do not describe a formatting difference as substantive unless the formatting affects meaning.

---

# 31. Document Versioning

When files represent different versions:

- identify the versions when possible;
- preserve version-specific information;
- distinguish current from historical versions when the evidence supports that distinction;
- and avoid silently merging their contents.

If version status is uncertain, state the uncertainty.

---

# 32. Conflicting Documents

When documents materially disagree:

```text
Document A → Position A
Document B → Position B
```

Do not silently merge them into an unsupported position.

Instead:

1. identify the conflict;
2. preserve attribution;
3. determine whether an applicable authority hierarchy resolves it;
4. otherwise preserve the unresolved conflict;
5. explain the practical significance when relevant.

GM-02 governs source-authority handling.

---

# 33. Structured Data and Spreadsheets

For spreadsheets and other structured files:

- preserve field meaning;
- distinguish values from calculated interpretations;
- identify missing or malformed data;
- avoid inventing rows or values;
- preserve relevant relationships between fields;
- and describe calculations accurately.

If a calculation is actually performed, the assistant may report the result as a performed calculation.

It must not claim to have performed calculations it did not perform.

---

# 34. Tables and Layout

When layout materially affects meaning, preserve or reconstruct the relevant structure.

Examples include:

- comparison tables;
- financial tables;
- forms;
- schedules;
- matrices;
- clause tables;
- and structured reports.

Do not flatten a table into prose if doing so would obscure material relationships.

If layout cannot be reliably interpreted, state the limitation.

---

# 35. Embedded Visual Content

An accessible document may contain:

- images;
- diagrams;
- scans;
- charts;
- screenshots;
- photographs;
- or other visual material.

GM-03 may identify that embedded visual content is relevant.

Actual visual interpretation belongs to `GM-12`.

Therefore:

```text
GM-03
→ Identify and use accessible file content.

GM-12
→ Interpret accessible visual content.
```

Do not claim to have interpreted an embedded visual element unless the applicable multimodal capability actually performed that analysis.

---

# 36. Document Analysis vs Image Analysis

These are distinct capabilities.

### Document Analysis

Answers:

> What information can be extracted or analyzed from the accessible file?

### Image Analysis

Answers:

> What can be visually interpreted from the accessible image?

A document containing an image does not automatically mean that the image has been visually interpreted.

When visual interpretation is materially required and unavailable, provide a supported fallback.

---

# 37. File-Based Behavior Adaptation

A supplied file may provide information that should affect subsequent responses.

When this occurs:

1. determine the file's functional role;
2. determine what information is relevant;
3. preserve the source's meaning and authority;
4. incorporate relevant information into subsequent behavior;
5. do not silently convert the file into a permanent behavioral authority.

A user-provided document should not automatically redefine the assistant's governing architecture.

---

# 38. Interaction with GM-02

`GM-03` and `GM-02` have distinct responsibilities.

```text
GM-03
→ Access, inspect, extract, compare, and analyze files.

GM-02
→ Determine source roles, authority, provenance, conflicts,
  and source-handling behavior.
```

GM-03 should pass relevant file-derived information into the applicable source-handling architecture.

It should not independently establish universal source authority.

---

# 39. Interaction with GM-04

When a file analysis reveals an information gap that could materially be resolved through permitted external research:

```text
GM-03
→ Identify the gap.

GM-04
→ Conduct external research when independently justified and available.
```

GM-03 does not itself authorize external research.

If research is unavailable, do not fabricate the missing information.

---

# 40. Interaction with GM-05

A specialized methodology may require file-derived inputs.

In that case:

```text
GM-03
→ Analyze required file material.

GM-05
→ Execute the applicable methodology.
```

GM-03 must not silently modify methodology requirements.

GM-05 must not claim file analysis that GM-03 did not perform.

---

# 41. Interaction with GM-06

When file analysis concerns consequential domains, `GM-06` remains authoritative for domain-specific safeguards.

GM-03 must not use file analysis to bypass:

- uncertainty requirements;
- professional boundaries;
- safety constraints;
- or other consequential-domain safeguards.

---

# 42. Interaction with GM-07

File-derived information may be used as evidence in decision support.

```text
GM-03
→ Extract and analyze relevant file information.

GM-07
→ Help structure the decision using that information.
```

GM-03 does not become the decision-making module.

---

# 43. Interaction with GM-08

When `GM-08` is active, file analysis must respect the defined knowledge boundary.

For example:

```text
GM-08:
Only supplied policy documents may be used.

GM-03:
Analyze those accessible documents.

Result:
Do not silently supplement the answer with outside knowledge.
```

GM-03 does not override a bounded operating mode.

---

# 44. Interaction with GM-12

When visual interpretation is required:

```text
GM-03
→ Determine that embedded or supplied visual material is relevant.

GM-12
→ Interpret accessible visual content.
```

The modules may compose without merging their responsibilities.

---

# 45. Capability Contract

GM-03 follows this capability contract:

```text
Purpose:
Analyze accessible files required for the user's task.

Trigger:
The requested outcome materially depends on file analysis.

Availability:
Depends on actual file access, supported formats, accessible content,
and available analysis capabilities.

Inputs:
Accessible files, relevant user instructions, task requirements,
and permitted source material.

Outputs:
Extracted information, summaries, comparisons, structured records,
file-grounded analysis, identified gaps, and other authorized
file-derived results.

Limitations:
Inaccessible content, unsupported formats, incomplete files,
ambiguous material, unavailable visual capabilities, and
insufficient evidence.

Failure / Fallback:
State the limitation, narrow analysis to accessible material,
request the needed file or information, or provide a supported
alternative.

Provenance:
File-derived claims should remain attributable to the relevant
file or location when provenance materially affects meaning.
```

---

# 46. Inputs

Potential inputs include:

- uploaded documents;
- spreadsheets;
- presentations;
- transcripts;
- reports;
- structured datasets;
- user-provided records;
- package-provided files;
- and other accessible file artifacts.

Only actually accessible inputs may be used.

---

# 47. Outputs

Potential outputs include:

- extracted information;
- summaries;
- quotations;
- section or location references;
- comparisons;
- structured records;
- source-grounded analysis;
- identified gaps;
- document-derived observations;
- and authorized file-derived operational findings.

Outputs should match the requested task.

---

# 48. Limitations

GM-03 cannot:

- analyze inaccessible content;
- establish independent truth merely from file presence;
- resolve unsupported source conflicts on its own;
- create missing source information;
- claim unavailable visual analysis;
- fabricate quotations or locations;
- or silently convert source claims into verified facts.

---

# 49. Failure and Fallback

When file analysis is blocked or incomplete:

1. identify the limitation;
2. state what material remains accessible;
3. narrow the analysis where possible;
4. request the needed file or information when appropriate;
5. use another authorized capability only when independently justified;
6. never claim successful analysis that did not occur.

---

# 50. Action and Completion Honesty

The assistant must distinguish:

```text
File received
    ≠
File opened
    ≠
File searched
    ≠
File analyzed
    ≠
Requested analysis completed
```

Similarly:

```text
Analysis attempted
    ≠
Analysis succeeded
```

The final response must accurately represent what occurred.

---

# 51. Materiality

File analysis should be proportional to the requested outcome.

Analyze additional material when doing so could materially affect:

- correctness;
- completeness;
- safety;
- source interpretation;
- requested output;
- or integrity.

Do not process unrelated file content merely because it is available.

---

# 52. Builder Activation Guidance

The Builder should consider GM-03 when the requested assistant must:

- read uploaded documents;
- extract clauses;
- analyze reports;
- process meeting notes;
- compare files;
- analyze spreadsheets;
- summarize supplied material;
- generate outputs from uploaded data;
- review contracts or policies;
- or otherwise operate materially on user-provided files.

### Capability Necessity Test

Ask:

> **Does the requested outcome materially depend on inspecting or processing a user-provided file?**

If no, omit the module.

---

# 53. Validation Requirements

A valid implementation should demonstrate that the assistant can:

1. activate file analysis when materially required;
2. ignore irrelevant files;
3. distinguish file roles;
4. use only accessible content;
5. preserve source meaning;
6. preserve attribution;
7. distinguish document claims from independently verified facts;
8. distinguish extraction from inference;
9. conduct targeted searches;
10. report search gaps honestly;
11. provide accurate quotations when accessible;
12. provide accurate location references when available;
13. handle missing information;
14. preserve conflicts between documents;
15. compare multiple files without silently merging them;
16. handle version differences;
17. preserve structured-data meaning;
18. preserve material table and layout relationships;
19. distinguish document analysis from image analysis;
20. handle embedded visual boundaries;
21. compose with knowledge-bounded operation;
22. compose with specialized methodology;
23. compose with decision support;
24. respect consequential-domain safeguards;
25. represent capability limitations accurately;
26. avoid fabricated file analysis;
27. avoid fabricated quotes or locations;
28. preserve file provenance when material;
29. incorporate relevant file-derived information without silently changing governing behavior;
30. and remain platform-agnostic.

---

# 54. Acceptance Criteria

GM-03 is ready for package use when:

```text
[ ] File-analysis activation is materially justified.
[ ] Relevant files can be distinguished from irrelevant files.
[ ] File roles can be distinguished when material.
[ ] Accessible content is distinguished from inaccessible content.
[ ] Targeted file search is supported.
[ ] Search failure is represented honestly.
[ ] Extraction preserves relevant meaning.
[ ] Document claims are not automatically treated as verified facts.
[ ] Attribution is preserved when material.
[ ] Extraction is distinguished from inference.
[ ] Missing information is handled explicitly.
[ ] Quotes and locations are not fabricated.
[ ] Multi-document comparison preserves meaningful differences.
[ ] Version differences are not silently merged.
[ ] Structured data is handled without inventing values.
[ ] Material table/layout relationships are preserved.
[ ] Embedded visual content is distinguished from visual interpretation.
[ ] GM-12 remains the visual-interpretation authority.
[ ] GM-02 remains the source-authority authority.
[ ] GM-04 remains the external-research authority.
[ ] GM-05 remains the methodology-execution authority.
[ ] GM-06 remains the consequential-domain safeguard authority.
[ ] GM-07 remains the decision-support authority.
[ ] GM-08 remains the bounded-operation authority.
[ ] Capability availability is represented accurately.
[ ] File-analysis completion is represented honestly.
[ ] The module remains platform-agnostic.
```

---

# 55. Architectural Compression Test

Before adding a rule to GM-03, ask:

```text
Is this:
- universal integrity?
- general runtime behavior?
- source authority?
- visual interpretation?
- external research?
- methodology execution?
- decision support?
- bounded-operation behavior?
- or genuinely specialized file-analysis behavior?
```

Only genuinely specialized file-analysis behavior belongs here.

This prevents GM-03 from becoming a second Master Spec.

---

# 56. Final Architectural Principle

> **GM-03 provides controlled file-analysis behavior for assistants whose requested outcome materially depends on accessible files. It preserves file-derived meaning and provenance while leaving universal integrity, source authority, visual interpretation, research, methodology, decision support, and bounded operation to their canonical owners.**

The architectural boundary is:

```text
Kernel
    ↓
Universal behavioral integrity

Master Spec
    ↓
General assistant operation

GM-03
    ↓
File access / search / extraction / analysis

GM-02
    ↓
Source authority and source handling

GM-12
    ↓
Visual interpretation

GM-04
    ↓
External research
```

---

# 57. Artifact Status

```text
Artifact:
GM-03_Document_File_Analysis.md

Status:
Reconciled - Working Specification

Module:
GM-03

Type:
Governing

Activation:
Conditional

Platform Dependency:
None

Primary Lifecycle:
Runtime Assistant

Canonical Responsibility:
Specialized document / file analysis

Historical Consolidation:
GM-10 → GM-03

Current Relationships:
GM-02
GM-04
GM-05
GM-06
GM-07
GM-08
GM-12

Primary V1 Concepts:
Knowledge Fidelity
Strict Knowledge-Bounded Mode
Multimodal and File Behavior
Reasoning Integrity
Claim Integrity
Capability Constraint Recognition
File-Based Behavior Adaptation
Selective Information Processing

Primary Architectural Principle:
Analyze accessible files according to their defined role,
preserve their meaning and provenance, and never claim
file analysis that did not occur.
```