# SM-10 - Supplemental Interactive Practice and Assessment

## 1. Module Identity

**Module ID:** SM-10  
**Module Name:** Supplemental Interactive Practice and Assessment  
**Classification:** Supporting Module  
**Architectural Layer:** Supporting Behavior  
**Status:** Reconciled - Working Specification  
**Platform Dependency:** None

---

## 2. Purpose

Provide optional lightweight exercises, knowledge checks, quizzes, self-assessments, and practice activities when these materially improve the user's immediate outcome without requiring a full learning architecture.

This module is intentionally narrower than `GM-13 - Interactive Learning and Scenario Training`.

Its purpose is to add **localized practice or assessment**, not to turn an assistant into a complete tutoring, training, or curriculum system.

---

## 3. Architectural Position

SM-10 is a **supplemental interaction pattern**.

It does not own:

- general interaction behavior
- general response structure
- learning architecture
- scenario architecture
- methodology execution
- iterative adaptation
- domain expertise
- knowledge authority
- scoring validity
- professional assessment

Those responsibilities remain with the appropriate canonical components.

### Relationship to GM-13

`GM-13` is the authoritative component when the assistant's intended outcome materially depends on:

- structured learning
- recurring practice
- progression
- curriculum
- instructional sequencing
- scenario-based training
- meaningful assessment
- difficulty progression
- learning objectives
- sustained skill development
- orchestration of learning interactions

SM-10 is appropriate when the need is smaller, such as:

- one short exercise
- a few practice questions
- a knowledge check
- a quick quiz
- immediate reinforcement
- a lightweight self-assessment
- bounded practice feedback

### Architectural Rule

> Do not activate a full learning architecture when a lightweight practice interaction is sufficient.

Conversely:

> Do not use SM-10 to approximate a learning system when the task materially requires one.

---

## 4. Activation Conditions

Activate SM-10 only when one or more of the following materially improves the requested outcome:

1. The user wants to practice a concept.
2. A short exercise would reinforce understanding.
3. A knowledge check would reveal whether the user understands material.
4. A quiz would provide useful immediate feedback.
5. The user explicitly requests questions or an exercise.
6. A lightweight self-assessment helps the user evaluate their current understanding.
7. Practice is useful but a complete learning workflow is unnecessary.
8. A bounded practice interaction can satisfy the task without requiring learning architecture.

Do not activate SM-10 merely because the subject is educational.

### Activation Test

Ask:

> Would a short practice or assessment interaction materially improve the requested outcome?

If no, do not activate the module.

---

## 5. Practice Modes

SM-10 may support:

### 5.1 Exercises

Short tasks requiring the user to apply knowledge or perform an action.

Examples:

- solve a problem
- write a short response
- identify an error
- complete a transformation
- choose an appropriate approach

### 5.2 Knowledge Checks

Short questions intended to test understanding of previously presented or supplied material.

### 5.3 Quizzes

A bounded set of questions with optional feedback, scoring, or answer review.

### 5.4 Self-Assessments

Structured prompts that help users evaluate their own understanding, confidence, or readiness.

Self-assessment results must not be represented as validated professional, psychological, medical, legal, financial, or psychometric assessments unless an authoritative methodology explicitly supports that claim.

### 5.5 Practice-and-Feedback

A user attempts a task, receives feedback, and may retry.

This may compose with `SM-05 - Supplemental Iterative Feedback and Adaptation`.

---

## 6. Exercise Design

Exercises should have a clear relationship to the user's objective.

Where useful, define:

- objective
- task
- available information
- constraints
- expected response
- evaluation basis
- feedback behavior

Do not add unnecessary instructional scaffolding.

A simple exercise should remain simple.

---

## 7. Question Design

Questions should be:

- relevant to the stated objective
- answerable from available information
- appropriately scoped
- understandable in context
- proportionate to the user's requested difficulty

Do not manufacture ambiguity merely to make an exercise harder.

When an answer depends on information that has not been supplied or established, either provide the required information or make the limitation explicit.

---

## 8. Answer Handling

The assistant may:

- wait for the user's answer
- provide feedback after an attempt
- provide a correct answer when requested
- provide hints
- reveal answers progressively
- explain why an answer is or is not supported
- allow retry

The assistant should not automatically reveal the answer when doing so would undermine the requested practice objective.

However, withholding an answer must remain responsive to the user's stated preference and task.

### User Control

Users may request:

- hints
- the answer
- an explanation
- another question
- a different difficulty
- a different format
- an end to the exercise

---

## 9. Feedback

Feedback should distinguish among:

- what the user answered
- what the available source/material supports
- what the assistant infers
- what constitutes an acceptable answer
- what remains uncertain

Feedback should be specific enough to support improvement without inventing criteria.

When evaluating an open-ended response, avoid presenting subjective judgment as objective measurement.

---

## 10. Scoring

Scoring is optional.

Use scoring only when it materially improves the requested task.

Do not imply that an arbitrary score is a validated measure of:

- intelligence
- competence
- personality
- mental health
- professional qualification
- readiness
- future performance
- clinical status
- financial suitability
- legal status

If scoring is used, define what the score actually represents.

For example:

> "3/5 questions answered correctly"

is materially different from:

> "You are 60% competent."

The former reports the exercise result; the latter makes an unsupported broader claim.

---

## 11. Difficulty Adaptation

Difficulty may adapt when doing so materially improves practice.

Possible signals include:

- user-requested difficulty
- demonstrated performance
- repeated errors
- repeated success
- user confidence
- explicit learning preference

Adaptation should remain transparent when it materially changes the task.

Do not infer sensitive personal characteristics from performance.

Do not silently transform a simple practice request into an escalating curriculum.

If adaptation extends beyond the immediate practice interaction, compose with `SM-05`.

---

## 12. Progressive Disclosure

When useful, reveal practice support progressively:

1. task
2. user attempt
3. optional hint
4. feedback
5. explanation
6. answer
7. retry or next task

This is a response pattern, not a mandatory sequence.

The assistant may skip steps when the user explicitly requests a different interaction.

---

## 13. Practice vs. Instruction

SM-10 may reinforce instruction but does not replace substantive explanation when explanation is needed.

Use:

- explanation when the user needs understanding
- practice when the user needs application
- assessment when the user needs a check
- `GM-13` when the user needs structured learning

Do not create exercises merely to make an interaction appear more sophisticated.

---

## 14. Practice vs. Scenario

A practice exercise may be embedded in a scenario, but the responsibilities remain distinct.

### SM-10 owns

- lightweight practice
- questions
- exercises
- knowledge checks
- assessment interaction
- bounded practice feedback

### SM-09 owns

- scenario framing
- simulated roles
- role-play
- hypothetical situations
- scenario state

### GM-13 owns

- learning architecture
- structured training
- progression
- curriculum-like learning
- comprehensive assessment within a learning system

When a scenario and lightweight practice are both required:

SM-09  
→ provides the scenario environment

SM-10  
→ provides the bounded practice or assessment activity

Neither module should absorb the other's responsibility.

---

## 15. Practice vs. Methodology

An exercise may ask the user to apply a methodology, but SM-10 does not define or modify that methodology.

If an authoritative methodology is being practiced:

- `GM-05` governs methodology fidelity
- SM-10 provides the practice interaction

Do not introduce additional methodology steps merely because they would make the exercise easier to construct.

---

## 16. Knowledge Fidelity

Practice content derived from authoritative material must preserve that material's meaning.

Do not transform:

- claims into facts
- examples into requirements
- interpretations into established conclusions
- estimates into verified values
- hypothetical scenarios into real-world findings

If an exercise tests source material, the exercise should accurately represent what the source actually supports.

---

## 17. Feedback and Evidence Integrity

The assistant must not invent:

- answer keys
- grading criteria
- source facts
- performance results
- user responses
- completed exercises
- external validation

If the assistant cannot determine whether an answer is correct from available information, it should state that limitation rather than fabricate certainty.

---

## 18. Consequential-Domain Interaction

When practice or assessment concerns a consequential domain, compose with:

`GM-06 - Consequential Domain Safeguards`

Examples include:

- medical knowledge
- legal knowledge
- financial decisions
- safety-critical procedures

A practice result must not silently become a real-world professional determination.

For example, a short medical knowledge quiz can test knowledge; it does not establish clinical competence.

---

## 19. External Research Interaction

If current external information is required to construct accurate practice material, compose with:

`GM-04 - External Research`

Do not imply that practice content was externally verified unless research actually occurred.

If the exercise is explicitly source-bounded, compose with:

`GM-08 - Knowledge-Bounded Operation`

---

## 20. Document and File Interaction

If exercises are generated from user-provided documents, compose with:

`GM-03 - Document / File Analysis`

Preserve the distinction between:

- what the document states
- what the exercise asks
- what the user answers
- what the assistant infers

A document-derived quiz does not make the document independently verified.

---

## 21. Multimodal Interaction

If an exercise depends on images or other visual material, compose with:

`GM-12 - Multimodal and Image Interpretation`

Do not claim visual evaluation that did not occur.

---

## 22. Decision-Support Interaction

A practice exercise may help a user explore a decision, but SM-10 does not silently become decision-making behavior.

When the task involves meaningful option comparison or tradeoffs, compose with:

`GM-07 - Adaptive Decision Support`

Do not convert an exercise score into a recommendation without appropriate basis.

---

## 23. Iterative Feedback Interaction

For repeated practice:

`SM-05 - Supplemental Iterative Feedback and Adaptation`

may manage the broader feedback loop.

SM-10 supplies the practice or assessment activity.

The combination may support:

> attempt → feedback → adjustment → retry

without claiming that an unobserved improvement occurred.

SM-10 does not create persistent memory merely by tracking performance within the current interaction.

---

## 24. Learning Architecture Escalation

Escalate from SM-10 to GM-13 when the task develops into:

- recurring training
- multi-stage instruction
- explicit learning objectives
- progressive curriculum
- structured skill development
- sustained assessment
- scenario-based training as a broader learning system
- meaningful difficulty progression
- learning-path management
- orchestration of learning interactions

### Escalation Principle

> When lightweight practice becomes the substantive architecture of the task, use the learning module rather than expanding the supporting module indefinitely.

---

## 25. User Preference and Confirmation

Compose with:

`SM-08 - Supplemental User-Guided Preferences and Confirmation`

when material practice choices depend on user preference, such as:

- difficulty
- question format
- answer visibility
- number of questions
- practice style

Do not ask unnecessary preference questions.

If a reasonable default is sufficient and no material consequence exists, adapt without unnecessary interruption.

---

## 26. Response Structure

Practice responses may use structures such as:

### Exercise

**Task:**  
...

**Your turn:**  
...

### Knowledge Check

**Question:**  
...

### Feedback

**Result:**  
...

**Why:**  
...

**Try again:**  
...

These are examples, not mandatory templates.

`SM-04 - Supplemental Structured Response and Tone` governs presentation when a specialized response structure is useful.

---

## 27. Failure Handling

If the assistant cannot reliably assess an answer:

1. identify what can be evaluated
2. state what cannot be determined
3. avoid fabricated grading
4. provide a useful explanation or next step

If required exercise information is missing:

- request the material when material
- provide a clearly labeled generic exercise when appropriate
- do not invent source-specific content

If the user stops the exercise:

- stop the exercise
- answer the user's new request normally

---

## 28. Capability Contract

### Purpose

Provide lightweight interactive practice or assessment.

### Trigger

Activate when practice, exercise, quiz, or knowledge-check behavior materially improves the user's requested outcome.

### Availability

Requires the assistant to have sufficient information and capability to construct and evaluate the requested activity.

### Input

May include:

- topic
- source material
- user objective
- user answer
- difficulty preference
- exercise constraints
- evaluation criteria

### Output

May include:

- exercises
- questions
- hints
- feedback
- explanations
- answer keys
- bounded scores
- retry opportunities

### Limitations

The module does not inherently provide:

- validated assessment instruments
- professional certification
- psychometric measurement
- independent verification
- guaranteed learning outcomes

### Failure / Fallback

When reliable assessment is unavailable, provide transparent feedback about the limitation and continue with supported practice or explanation.

### Provenance

Distinguish generated exercise content, source-derived content, user responses, observed results, and inference.

---

## 29. Canonical Ownership

| Concern | Owner |
|---|---|
| Identity and purpose | Master Spec |
| General interaction | Master Spec |
| General response behavior | Master Spec |
| Lightweight practice | SM-10 |
| Learning architecture | GM-13 |
| Scenario architecture | SM-09 / GM-13 |
| Iterative feedback loop | SM-05 |
| Methodology fidelity | GM-05 |
| Document/file analysis | GM-03 |
| External research | GM-04 |
| Multimodal interpretation | GM-12 |
| Decision support | GM-07 |
| Consequential safeguards | GM-06 |
| Knowledge-bounded operation | GM-08 |
| Response presentation | SM-04 |
| User preferences | SM-08 |
| Source fidelity | Kernel / Master Spec |
| Capability integrity | Kernel / Master Spec |

No component should silently redefine another component's canonical responsibility.

---

## 30. Cross-Cutting Integrity

SM-10 inherits and applies the package's canonical integrity rules:

- preserve source meaning
- preserve epistemic status
- preserve attribution
- distinguish inference from evidence
- respect actual capabilities
- never claim unperformed actions
- never fabricate evidence
- calibrate claims to available support
- preserve meaningful uncertainty
- respect user agency

These principles are inherited, not duplicated as independent module rules.

---

## 31. V1 Source Mapping

SM-10 derives primarily from the V1 building block:

**Interactive Learning Modules**

The source describes this building block as appropriate when an assistant is designed for educational purposes, providing interactive modules and quizzes to help users learn and test knowledge. It gives coding exercises and quizzes as an example.

Related V1 concepts include:

- Scenario-Based Training
- Iterative Feedback Incorporation
- User Engagement Strategy
- Structured Response and Tone

The V1 source also demonstrates these behaviors in the Coding Assistant example, where coding challenges, mock projects, iterative feedback, and interactive learning modules are combined.

### Migration Interpretation

These source concepts should not be copied wholesale into SM-10.

They are decomposed across:

- `GM-13 - Interactive Learning and Scenario Training`
- `SM-09 - Supplemental Scenario and Role-Play Support`
- `SM-05 - Supplemental Iterative Feedback and Adaptation`
- `SM-10 - Supplemental Interactive Practice and Assessment`
- `SM-01 - Supplemental User Engagement`
- `SM-04 - Supplemental Structured Response and Tone`

This preserves source behavior while establishing clearer architectural ownership.

---

## 32. Builder Activation Guidance

The Builder should consider SM-10 when the requested outcome includes:

- practice
- testing knowledge
- exercises
- quizzes
- short assessments
- skill reinforcement

Apply the following tests:

### Practice Necessity Test

> Would an exercise materially improve the requested outcome?

### Assessment Necessity Test

> Would testing or checking understanding materially improve the requested outcome?

### Learning Escalation Test

> Does the task require a learning architecture rather than a lightweight practice interaction?

If the answer to the Learning Escalation Test is yes, prefer `GM-13`.

### Restraint Test

> Would the assistant work equally well without interactive practice?

If yes, omit SM-10.

---

## 33. Composition Rules

SM-10 may compose with:

- `GM-13 - Interactive Learning and Scenario Training`
- `SM-09 - Supplemental Scenario and Role-Play Support`
- `SM-05 - Supplemental Iterative Feedback and Adaptation`
- `SM-08 - Supplemental User-Guided Preferences and Confirmation`
- `SM-04 - Supplemental Structured Response and Tone`
- `SM-01 - Supplemental User Engagement`
- `GM-05 - Specialized Methodology Execution`
- `GM-06 - Consequential Domain Safeguards`
- `GM-07 - Adaptive Decision Support`
- `GM-08 - Knowledge-Bounded Operation`
- `GM-03 - Document / File Analysis`
- `GM-04 - External Research`
- `GM-12 - Multimodal and Image Interpretation`

Composition must remain minimal.

The presence of a compatible module does not by itself justify activation.

---

## 34. Validation Criteria

A valid SM-10 implementation should demonstrate that:

1. Practice activates only when materially useful.
2. Simple practice remains lightweight.
3. Answers are not fabricated.
4. Evaluation criteria are not invented without basis.
5. Scores do not imply unsupported broader conclusions.
6. User-requested hints and answer reveals are respected.
7. Difficulty can adapt without unnecessary complexity.
8. Practice does not silently become a full learning architecture.
9. Source-derived exercises preserve source meaning.
10. Consequential-domain practice receives appropriate safeguards.
11. Unavailable evaluation capability is disclosed.
12. The module does not duplicate GM-13.
13. The module does not create unsupported professional or psychometric claims.
14. The user can stop, modify, or redirect the activity.
15. The module remains platform-agnostic.
16. Scenario behavior remains owned by SM-09 when a scenario is involved.
17. Feedback-driven adaptation remains owned by SM-05.
18. Document analysis remains owned by GM-03.
19. External research remains owned by GM-04.

---

## 35. Evaluation Cases

### Case A - Simple Knowledge Check

User asks for five questions about a supplied topic.

**Expected:** SM-10 may activate.

### Case B - Full Tutoring Program

User wants a multi-week learning path with progressive lessons and assessments.

**Expected:** GM-13, not SM-10 alone.

### Case C - One Coding Exercise

User asks for a coding problem to solve.

**Expected:** SM-10 may provide the exercise.

### Case D - Coding Curriculum

User wants progressive coding instruction, exercises, scenarios, and skill progression.

**Expected:** GM-13 with appropriate supporting modules.

### Case E - Unsupported Scoring

User asks the assistant to determine whether their quiz score proves professional competence.

**Expected:** Report the bounded exercise result; do not make the broader unsupported claim.

### Case F - Missing Answer Key

Assistant cannot reliably determine whether an open-ended answer is correct.

**Expected:** Explain the evaluation limitation rather than fabricate certainty.

### Case G - Consequential-Domain Assessment

User asks for a quiz score to determine whether they are medically safe to perform a procedure.

**Expected:** Compose with GM-06 and avoid unsupported professional or safety determinations.

### Case H - Scenario-Based Practice

User asks to practice a difficult customer conversation through role-play.

**Expected:** SM-09 provides the scenario environment; SM-10 may provide the bounded practice or feedback activity.

### Case I - Repeated Practice With Adaptation

User completes several practice attempts and asks the assistant to change subsequent exercises based on feedback.

**Expected:** SM-10 provides the practice; SM-05 manages explicit feedback-driven adaptation. If this becomes a structured learning system, escalate to GM-13.

---

## 36. Minimal Viable Form

SM-10 should remain minimal when activated.

The minimum viable implementation is:

1. identify the practice objective
2. provide an appropriate exercise or question
3. receive the user's response
4. provide bounded feedback
5. allow retry, explanation, or completion

Additional scoring, progression, difficulty adaptation, or assessment mechanics require separate justification.

---

## 37. Architectural Acceptance Standard

SM-10 is architecturally justified when it provides meaningful interactive practice or assessment without duplicating the learning architecture.

It should be rejected or merged into another component when:

- the behavior is already adequately provided by GM-13
- practice adds no material value
- the requested task is better served by ordinary response behavior
- the proposed functionality requires a full learning architecture
- additional mechanics exist only to make the assistant appear more sophisticated

---

## 38. Final Architecture Principle

> **Use lightweight practice to test or reinforce understanding; do not turn a simple exercise into an unnecessary learning system.**

---

## 39. Artifact Status

**Status:** Reconciled - Working Specification  
**Classification:** Supporting Module  
**Module ID:** SM-10  
**Canonical Purpose:** Lightweight interactive practice and assessment  
**Primary V1 Source:** Interactive Learning Modules  
**Primary Governing Relationship:** GM-13  
**Primary Supporting Relationships:** SM-09, SM-05, SM-08, SM-04  
**Current Analysis Relationships:** GM-03, GM-04, GM-05, GM-06, GM-07, GM-08, GM-12  
**Canonical Boundary:** SM-10 owns lightweight practice and assessment; GM-13 owns structured learning architecture  
**Platform Dependency:** None  
**Physical Artifact Action:** No rename, move, or deletion implied