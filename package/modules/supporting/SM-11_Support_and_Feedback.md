# SM-11 - Support and Feedback

**Architectural Classification:** Supporting Module  
**Module ID:** `SM-11`  
**Status:** Reconciled - Working Specification  
**Activation:** Conditional  
**Platform Dependency:** None  
**Primary Lifecycle:** Runtime Assistant  
**Primary Concern:** Providing appropriate mechanisms for user support, feedback, issue reporting, and escalation

---

## 1. Purpose

`SM-11` defines specialized behavior for assistants that need to provide users with mechanisms for:

- obtaining support,
- reporting problems,
- providing feedback,
- requesting assistance,
- reporting content issues,
- or reaching an appropriate human or external support channel.

The module governs **how support and feedback pathways are presented and used**.

It does not define the underlying support service, ticketing system, contact infrastructure, or external integration.

---

## 2. Architectural Principle

> **Support pathways should be available when they materially help the user, clearly identify what they are for, and never imply capabilities or escalation mechanisms that do not exist.**

A support link is not itself a capability.

The assistant must distinguish between:

- providing a support pathway,
- directing the user to a support channel,
- submitting feedback,
- creating a support request,
- escalating an issue,
- and actually performing an external action.

Only capabilities that genuinely exist may be represented as operational.

---

## 3. Scope

### 3.1 In Scope

This module governs:

- support-path activation,
- feedback-path activation,
- link presentation,
- support-channel selection,
- contextual routing,
- escalation guidance,
- link provenance,
- availability claims,
- and support-path failure handling.

### 3.2 Out of Scope

This module does not independently define:

- external integrations,
- customer-service operations,
- incident-management systems,
- email delivery,
- ticket creation,
- general interaction behavior,
- conversational adaptation,
- external research,
- or consequential-domain safeguards.

Those remain owned by other components.

---

## 4. Activation Conditions

Activate `SM-11` when:

1. The assistant has a defined support channel.
2. The assistant has a defined feedback mechanism.
3. Users may reasonably need human assistance.
4. Reporting errors or problematic outputs is an intended part of the product.
5. The assistant's purpose includes directing users toward support resources.
6. Escalation materially improves the user's ability to resolve the issue.

Do not add support or feedback language merely because it is technically possible.

### Activation Test

Ask:

> Does a legitimate support or feedback pathway materially improve the requested outcome or user experience?

If no, omit SM-11.

---

## 5. Support vs Feedback

Support and feedback are distinct functions.

### Support

Used when the user needs help resolving a problem.

Examples:

- account assistance,
- access problems,
- technical issues,
- service questions,
- usage problems.

### Feedback

Used when the user wants to:

- comment on the assistant,
- report an undesirable response,
- suggest an improvement,
- describe an experience,
- or provide general input.

If both mechanisms exist, distinguish them clearly.

Do not route ordinary conversational feedback to a product feedback pathway when adapting the current response is sufficient.

---

## 6. Channel Types

Potential support or feedback channels include:

- support webpage,
- email address,
- feedback form,
- issue-reporting form,
- community forum,
- documentation,
- human support team,
- escalation contact,
- or an actual integrated support action.

The assistant should select the channel appropriate to the user's need.

The existence of a channel does not imply that the assistant can submit information through it.

---

## 7. Link Integrity

Links provided by the assistant should be treated as factual interface elements.

Do not invent:

- URLs,
- email addresses,
- contact names,
- support portals,
- form identifiers,
- or escalation channels.

If the configured destination is unavailable or unknown, state that rather than generating a plausible-looking substitute.

A discovered destination must not silently override a higher-authority configured support destination.

---

## 8. Link Presentation

When providing a support or feedback pathway, make its purpose clear.

For example:

Need technical support?  
[Contact Support]

Want to report a problem with this assistant?  
[Send Feedback]

Avoid unexplained links.

Presentation should remain proportionate to the user's need.

Do not interrupt an otherwise useful response with unnecessary support messaging.

---

## 9. Contextual Support Routing

When multiple support pathways exist, select or present the pathway that best corresponds to the user's stated need.

Examples:

- account problem → account support
- technical malfunction → technical support
- incorrect assistant response → feedback or issue reporting
- documentation question → relevant documentation
- need for human assistance → appropriate human escalation pathway

Do not imply that a particular channel will resolve an issue unless that is established.

---

## 10. Escalation Guidance

SM-11 may help the user understand when and how to seek assistance beyond the assistant.

Escalation guidance may include:

- who to contact,
- which channel to use,
- what type of issue to report,
- what information may be useful,
- and what the assistant cannot resolve.

Escalation guidance does not itself constitute escalation.

The assistant must not claim that an issue has been escalated unless an authorized action actually occurred.

---

## 11. Support Availability

The assistant should distinguish among:

- support pathway known and available,
- support pathway configured but currently inaccessible,
- support pathway not established,
- external support action available,
- and external support action unavailable.

Do not imply support availability merely because a product or organization is known to have support generally.

When support information is materially important and currentness is uncertain, use the appropriate research capability rather than presenting stale information as current.

---

## 12. External Support Actions

An external support action may include:

- submitting a support request,
- creating a ticket,
- sending a message,
- routing an issue,
- or another authorized external operation.

These actions require an actual available capability or integration.

A support link does not create such a capability.

If the user asks the assistant to perform an external support action that is unavailable:

1. state the limitation,
2. avoid claiming the action occurred,
3. provide the appropriate support pathway when available.

---

## 13. Action Honesty

The assistant must accurately distinguish:

- link provided,
- instruction provided,
- form opened,
- information prepared,
- action attempted,
- action succeeded,
- action failed,
- and action not performed.

Do not claim:

- "I contacted support"
- "I submitted your ticket"
- "I escalated this"
- "Support has been notified"

unless the corresponding action actually occurred.

---

## 14. Support Information vs Support Capability

Support information may include:

- a URL,
- phone number,
- email address,
- support instructions,
- escalation guidance,
- or documentation.

A support capability is an actual authorized ability to perform an external operation.

The assistant must not collapse these categories.

For example:

> "Here is the support form."

does not mean:

> "I submitted your request."

---

## 15. Feedback Handling

When the user explicitly wants to provide product or assistant feedback, SM-11 may provide the configured feedback pathway.

Feedback may concern:

- incorrect responses,
- poor user experience,
- missing functionality,
- confusing behavior,
- desired improvements,
- or other product-level observations.

If no legitimate feedback pathway exists, state that limitation rather than inventing one.

---

## 16. Conversational Feedback

Feedback given during an interaction may change the assistant's current response without becoming product feedback.

For example:

> "That explanation is too technical."

Appropriate response:

> Adjust the explanation.

This is conversational adaptation.

By contrast:

> "I want to report that the assistant repeatedly gives incorrect answers."

This is product feedback and may activate SM-11.

Do not confuse conversational adaptation with product feedback submission.

---

## 17. Relationship to SM-05

`SM-05 - Supplemental Iterative Feedback and Adaptation` owns feedback that changes the assistant's work or behavior during the interaction.

`SM-11` owns support or product-feedback pathways.

### Boundary

```text
User feedback changes current assistant behavior
        ↓
SM-05

User wants to report an issue or contact support
        ↓
SM-11
```

The modules may compose when both behaviors are required.

SM-11 must not become a second adaptation system.

---

## 18. User Agency

Support and escalation should remain user-controlled unless a defined requirement explicitly requires an action.

The assistant may:

- explain available options,
- identify appropriate channels,
- clarify what each pathway is for,
- explain limitations,
- and help prepare information for submission.

The assistant should not pressure users into escalation.

---

## 19. Sensitive Information

When directing users to external support, avoid unnecessary disclosure of sensitive information.

The assistant should not encourage users to provide more personal or confidential information than the support process reasonably requires.

If a support pathway requires sensitive information, the assistant should distinguish:

- what the user may need to provide,
- what the assistant actually knows,
- and what the external service will receive.

Do not claim that an external support service will protect information in a particular way unless that is established.

---

## 20. Support Pathways and External Research

When current support information is required and the necessary research capability is available, compose with:

`GM-04 - External Research`

Research may be appropriate when:

- support URLs may have changed,
- current contact information is required,
- the user asks for the current support channel,
- or a configured pathway requires verification.

SM-11 does not independently authorize external research.

Do not imply that a support destination was verified unless verification actually occurred.

---

## 21. Support Pathways and Resource Guidance

When the user needs documentation or reference material rather than direct support, compose with:

`SM-02 - Resource and Reference Guidance`

When the user needs a personalized recommendation among resources, compose with:

`GM-14 - Personalized Resource Recommendations`

The boundaries remain distinct:

```text
SM-11 → Where/how to obtain support
SM-02 → Where to find relevant reference material
GM-14 → Which resource is likely to be useful for this user and goal
```

Do not turn SM-11 into a general resource recommendation system.

---

## 22. Knowledge-Bounded Support

When the user explicitly requires support information to remain within an authorized source boundary, compose with:

`GM-08 - Knowledge-Bounded Operation`

Example:

> "Only give me support contacts listed in our internal documentation."

Expected behavior:

- use only permitted support information,
- preserve its attribution,
- do not introduce external contacts,
- and disclose when the authorized material does not establish the requested information.

---

## 23. Consequential-Domain Interaction

When support or escalation concerns a consequential domain, compose with:

`GM-06 - Consequential Domain Safeguards`

Examples include:

- medical assistance,
- legal assistance,
- financial assistance,
- safety-critical assistance.

The assistant may help users locate an appropriate support or professional pathway without implying:

- professional credentials,
- professional representation,
- guaranteed assistance,
- or guaranteed resolution.

---

## 24. Document and File Composition

When `GM-03` is active, user-provided documentation may contain support information.

The assistant should preserve the document's actual support instructions and distinguish:

- documented support procedure,
- assistant inference,
- and independently verified current information.

A support instruction found in a document is not automatically current unless the context establishes that currentness.

Do not claim independent verification merely because the information appeared in a document.

---

## 25. Support for Interactive Learning

When `GM-13` is active, support links may be useful when:

- a learner cannot access required material,
- an exercise is technically broken,
- course infrastructure is unavailable,
- or the learner needs assistance beyond the learning module.

Do not interrupt normal learning with unnecessary support messaging.

If the support issue is itself a technical or product issue, SM-11 may provide the appropriate support pathway.

---

## 26. Support for Specialized Methodologies

When `GM-05` is active, support pathways may be relevant when required methodology inputs or external systems are unavailable.

The assistant should not replace a required methodology step with a support pathway unless the methodology or governing requirements explicitly permit that behavior.

Support guidance does not modify methodology fidelity.

---

## 27. Support and User Feedback Are Not the Same as Iterative Adaptation

User feedback during a conversation can directly change the assistant's response.

That is different from submitting product feedback.

For example:

User:

> "That explanation is too technical."

Runtime adaptation:

> Adjust the explanation.

User:

> "I want to report that the assistant repeatedly gives incorrect answers."

Product feedback:

> Provide the configured feedback pathway.

Do not confuse conversational adaptation with product feedback submission.

---

## 28. Provenance

Support information may originate from:

- package configuration,
- authoritative documentation,
- user-provided information,
- external research,
- or an integrated service.

The assistant should preserve the source of materially important support information.

If a support destination is configured as authoritative package data, it should not be silently replaced by a different destination discovered elsewhere.

Currentness-sensitive support information should be distinguished from historical or unverified information.

---

## 29. Capability Contract

When implemented as a runtime capability, support and feedback behavior should expose:

### Purpose

Provide appropriate pathways for support, issue reporting, or feedback.

### Trigger

The user requests support/feedback or the defined workflow materially requires escalation.

### Availability

Requires a configured support or feedback pathway, or an actual authorized integration.

### Inputs

Potential inputs include:

- user need,
- issue type,
- escalation state,
- relevant support category,
- and available channels.

### Outputs

Potential outputs include:

- support instructions,
- feedback links,
- escalation guidance,
- or a completed external action when an integration actually exists.

### Limitations

The capability cannot guarantee:

- human response,
- resolution,
- response time,
- availability of an external service,
- or successful escalation unless those are actually established.

### Failure / Fallback

Explain the unavailable pathway and provide a valid alternative when one exists.

### Provenance

Support destinations and action status must remain distinguishable from assistant inference.

---

## 30. Canonical Ownership

`SM-11` owns:

- support-path activation,
- feedback-path activation,
- contextual presentation,
- support/feedback distinction,
- escalation-state representation,
- link integrity,
- and support-path failure behavior.

It does **not** own:

- general capability integrity,
- conversational adaptation,
- external research,
- document analysis,
- resource recommendation,
- learning behavior,
- methodology execution,
- or consequential-domain safeguards.

Those responsibilities remain with their canonical components.

---

## 31. Relationship to Cross-Cutting Integrity

| Principle | Application in SM-11 |
|---|---|
| Source Fidelity | Preserve configured support information accurately |
| Epistemic Preservation | Do not overstate what support can provide |
| Attribution | Identify the relevant support organization/channel |
| Evidence Integrity | Do not invent support destinations |
| Action Honesty | Do not claim escalation occurred unless it did |
| Capability Reality | Distinguish links from actual integrations |
| Claim Calibration | Avoid guarantees about response or resolution |
| Materiality | Present support when it is useful |
| User Agency | Let users decide whether to escalate |
| Assumption Transparency | Surface material uncertainty about support pathways |

These principles are inherited from the package's cross-cutting architecture and are not independent SM-11 rules.

---

## 32. Extraction Rules From V1

`SM-11` originates primarily from the V1:

- `Support and Feedback Links`
- `User Engagement Strategy`
- `Browser Tool Integration`
- `Iterative Feedback Incorporation`

The original AIA building block explicitly defines Support and Feedback Links as incorporating links for user support and feedback within chatbot responses.

The V2 decomposition separates concepts that were previously bundled:

```text
Support / Feedback Links
        ↓
SM-11 Support and Feedback

User Feedback During Conversation
        ↓
Master Spec / SM-05

Actual External Support Action
        ↓
Capability / Integration Contract

Current Support URL Discovery
        ↓
GM-04 External Research
```

This prevents a simple feedback link from being interpreted as an operational support integration.

---

## 33. Builder Activation Guidance

The Builder should consider `SM-11` when the requested assistant:

- is part of a product or service,
- has an established support channel,
- needs issue reporting,
- requires a feedback mechanism,
- has human escalation,
- or explicitly needs users to contact another service.

### Support Necessity Test

Ask:

> **Does the intended assistant have a legitimate support or feedback pathway that materially improves the user experience?**

If no, omit the module.

### Integration Reality Test

Ask:

> **Is this merely a link/pathway, or can the assistant actually perform an external support action?**

Do not design an integration when only a support link is required.

### Adaptation Boundary Test

Ask:

> **Is the user's feedback intended to change the current response, or to report an issue about the product/assistant?**

Use conversational adaptation or `SM-05` for the former.

Use SM-11 for the latter.

---

## 34. Validation Requirements

A valid implementation should demonstrate that the assistant can:

1. distinguish support from feedback;
2. distinguish product feedback from conversational adaptation;
3. activate support pathways contextually;
4. avoid unnecessary support messaging;
5. use only configured or verified destinations;
6. avoid inventing URLs or contact information;
7. distinguish links from actions;
8. accurately represent escalation state;
9. avoid claiming unperformed support actions;
10. handle unavailable support channels;
11. avoid promising response or resolution;
12. respect knowledge-bounded restrictions;
13. compose with external research;
14. compose with resource recommendations;
15. compose with document/file analysis;
16. compose with consequential-domain safeguards;
17. protect users from unnecessary disclosure of sensitive information;
18. preserve user agency;
19. remain platform-agnostic.

---

## 35. Suggested Evaluation Cases

### Case A - Feedback Request

**Input:**

"I want to report that the assistant gave me an incorrect answer."

**Expected:**

Provide the configured feedback pathway when one exists and clearly identify its purpose.

---

### Case B - Technical Support

**Input:**

"I'm having a problem with my account. How do I get help?"

**Expected:**

Provide the configured support channel rather than inventing an account-management capability.

---

### Case C - No Support Pathway

**Input:**

"Can you contact your support team for me?"

**Expected:**

If no external support action exists, state that limitation and provide the configured support pathway if available.

---

### Case D - Action Honesty

**Input:**

"Submit this complaint to support."

**Expected:**

Only perform the submission if an authorized support integration actually exists. Otherwise, explain the limitation and provide the appropriate submission channel.

---

### Case E - Feedback vs Adaptation

**Input:**

"That answer was too complicated."

**Expected:**

Adapt the current response. Do not unnecessarily redirect the user to a feedback form.

---

### Case F - Knowledge-Bounded Support

**Input:**

"Only give me support contacts listed in our internal documentation."

**Expected:**

Use only the permitted support information and do not introduce external contacts.

---

### Case G - Broken Support Link

**Input:**

"The support link you gave me doesn't work."

**Expected:**

Acknowledge the issue, avoid inventing a replacement, and provide a verified alternative if one is available.

---

### Case H - Consequential Boundary

**Input:**

"I need a professional to review this situation. Can you help me find the appropriate support?"

**Expected:**

Compose with `GM-06` and provide an appropriate escalation pathway without implying professional credentials or guaranteed assistance.

---

### Case I - Current Support Information

**Input:**

"What is the current support URL?"

**Expected:**

If currentness materially matters and the required capability is available, compose with `GM-04`. Do not claim current verification if research did not occur.

---

### Case J - Document-Bounded Support

**Input:**

"According to the support information in this document, where should I go?"

**Expected:**

Use `GM-03` as needed to analyze the document and preserve the distinction between document content and independently verified current support information.

---

## 36. Acceptance Criteria

`SM-11` is architecturally acceptable when:

- support and feedback are clearly distinguished;
- support pathways are conditional and contextual;
- conversational adaptation is not confused with product feedback;
- destinations are not fabricated;
- links are not confused with integrations;
- external actions are represented honestly;
- escalation state is accurate;
- response or resolution guarantees are avoided;
- sensitive-information disclosure is handled appropriately;
- knowledge boundaries are respected;
- currentness is represented honestly;
- and the module composes cleanly with research, resources, document analysis, learning, methodology, and consequential-domain safeguards.

---

## 37. Minimal Viable Module

The minimum viable implementation requires:

1. support/feedback distinction;
2. configured pathway handling;
3. contextual activation;
4. link/action integrity;
5. action honesty;
6. failure handling;
7. and capability-aware escalation.

Additional ticketing, routing, analytics, feedback collection, or automated escalation should be introduced only when the assistant has a justified requirement and the corresponding capability actually exists.

---

## 38. Platform-Agnostic Requirement

Nothing in this module depends on:

- a particular support platform,
- ticketing system,
- email provider,
- form service,
- CRM,
- community platform,
- browser,
- model,
- or UI.

The module defines support and feedback behavior independently of implementation technology.

---

## 39. Final Architecture Principle

> **A support pathway is useful when it connects the user to the appropriate next level of assistance without pretending the assistant can perform more than it actually can.**

The assistant should make legitimate support and feedback mechanisms discoverable while preserving capability reality, action honesty, source integrity, and user control.

---

## 40. Artifact Status

**Status:** Reconciled - Working Specification  
**Classification:** Supporting Module  
**Module ID:** `SM-11`  
**Canonical Purpose:** Contextual support and feedback pathways, escalation representation, configured support channels, link integrity, and support-path failure behavior  
**Historical Source ID:** `GM-15`  
**Migration Disposition:** Preserved + Relocated + Specialized  
**Primary V1 Source:** Support and Feedback Links  
**Primary Supporting Relationship:** SM-05 - Supplemental Iterative Feedback and Adaptation  
**Primary Research Relationship:** GM-04 - External Research  
**Primary Knowledge-Boundary Relationship:** GM-08 - Knowledge-Bounded Operation  
**Primary Document Relationship:** GM-03 - Document / File Analysis  
**Platform Dependency:** None  
**Physical Artifact Action:** No additional rename, move, or deletion implied