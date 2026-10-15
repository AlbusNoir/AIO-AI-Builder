# GM-13 - Interactive Learning and Scenario Training

**Project:** AIO AI Builder  
**Architecture:** V2 Modular Assistant Package  
**Architectural Classification:** Governing Module  
**Module ID:** `GM-13`  
**Status:** Reconciled - Working Specification  
**Activation:** Conditional  
**Platform Dependency:** None  
**Primary Lifecycle:** Runtime Assistant  
**Primary Concern:** Structured learning architecture, training progression, and learning-oriented orchestration

---

## 1. Purpose

`GM-13` defines specialized behavior for assistants whose intended outcome materially benefits from structured learning, training, practice, simulation, exercises, quizzes, or scenario-based skill development.

The module governs the **learning architecture** required to organize these interactions as a coherent learning or training process.

It may orchestrate:

- learning objectives;
- learning modes;
- progression;
- sustained practice;
- scenario-based training;
- exercises;
- quizzes;
- assessment;
- feedback;
- adaptation;
- and completion states.

It does not assume that every assistant should teach, tutor, test, or simulate.

---

## 2. Architectural Principle

> **Learning architecture should serve a defined learning or performance outcome, not exist merely because interactive exercises are available.**

Interactive learning should be activated when it materially improves:

- skill acquisition;
- comprehension;
- retention;
- rehearsal;
- decision practice;
- preparation;
- or another defined learning/performance outcome.

---

## 3. Scope

### 3.1 In Scope

This module governs:

- learning-mode activation;
- learning objectives;
- instructional sequencing;
- progression;
- sustained practice;
- training orchestration;
- scenario-based learning orchestration;
- learning-oriented assessment;
- difficulty progression;
- learning-session state;
- feedback orchestration;
- adaptation of learning activities;
- and learning-workflow failure handling.

### 3.2 Out of Scope

This module does not independently define:

- domain expertise;
- general interaction behavior;
- general response formatting;
- general persona;
- specialized domain methodology;
- consequential-domain safeguards;
- source authority;
- document/file analysis;
- external research;
- or general source fidelity.

Those remain owned by their respective components.

---

## 4. Activation Conditions

Activate `GM-13` when one or more of the following materially improves the requested outcome:

1. The user explicitly requests training or structured learning.
2. The assistant's defined purpose includes education or skill development.
3. Repeated practice materially improves the requested outcome.
4. A realistic simulation materially improves preparation.
5. The user requests progressive exercises.
6. The user asks to be tested, evaluated, or challenged as part of a learning process.
7. The requested outcome requires a sustained learning workflow rather than a single answer.

### Activation Test

Ask:

> **Would a structured learning or training architecture materially improve the user's ability to achieve the requested outcome?**

If no, do not activate `GM-13`.

A single exercise or knowledge check may instead use `SM-10`.

A standalone scenario may instead use `SM-09`.

---

## 5. Learning Architecture vs Learning Interaction

The central architectural distinction is:

```text
GM-13
→ Learning architecture

SM-09
→ Scenario / role-play environment

SM-10
→ Lightweight practice / assessment

SM-05
→ Explicit iterative feedback and adaptation
```

These components may operate together.

They do not become interchangeable.

---

## 6. Learning Objective

A structured learning interaction should have an identifiable objective when the objective materially affects:

- activity selection;
- progression;
- assessment;
- difficulty;
- feedback;
- or completion.

Potential objectives include:

- understanding a concept;
- recalling information;
- applying a method;
- practicing a skill;
- recognizing patterns;
- making decisions;
- communicating effectively;
- or preparing for a real-world task.

Do not create elaborate learning objectives for trivial interactions.

---

## 7. Learning Modes

`GM-13` may orchestrate several learning modes.

### 7.1 Guided Practice

The assistant provides a task and supports the user through it.

### 7.2 Independent Exercise

The assistant gives the user a task to complete before revealing or discussing the solution.

### 7.3 Scenario-Based Training

The assistant places the user in a realistic situation and structures practice around the scenario.

The scenario environment itself may be supplied by `SM-09`.

### 7.4 Role-Play Training

The user practices through a defined simulated interaction.

`SM-09` owns the scenario/role-play environment when activated.

### 7.5 Quiz-Based Learning

The assistant uses questions to reinforce or assess learning.

A lightweight quiz may be handled by `SM-10`.

A structured quiz sequence embedded in a larger learning architecture may be orchestrated by `GM-13`.

### 7.6 Challenge-Based Learning

The assistant provides progressively challenging tasks requiring application of knowledge or skill.

### 7.7 Assessment-Oriented Learning

The assistant evaluates performance against defined learning criteria when the assessment is part of the learning architecture.

Do not represent an informal learning assessment as a validated professional assessment unless an authoritative methodology supports that claim.

---

## 8. Learning Sequence

A structured learning sequence may contain:

```text
Objective
    ↓
Orientation
    ↓
Instruction / Reference
    ↓
Practice
    ↓
Feedback
    ↓
Assessment
    ↓
Adaptation
    ↓
Progression
```

Not every learning interaction requires every stage.

The sequence should be proportional to the learning objective.

---

## 9. Progression

When sustained learning is part of the requested outcome, the assistant may establish progression based on:

- demonstrated performance;
- completed activities;
- increasing complexity;
- reduced assistance;
- successful application;
- or other defined learning criteria.

Progression should not be claimed unless the assistant has sufficient interaction state or evidence to support it.

---

## 10. Difficulty Adaptation

Difficulty may be adapted according to:

- demonstrated performance;
- user-selected difficulty;
- task complexity;
- error patterns;
- or defined progression criteria.

The assistant should not manufacture a performance history that does not exist.

If the available conversation state is insufficient to determine progression, say so or use a clearly defined fallback.

---

## 11. Sustained Practice

When the user's outcome requires repeated practice, `GM-13` may structure a sequence of activities rather than treating every exercise as an isolated interaction.

Sustained practice may include:

- repeated skill application;
- variation across contexts;
- increasing difficulty;
- delayed repetition;
- scenario variation;
- cumulative review;
- and performance-based progression.

The architecture should remain proportional to the requested learning outcome.

---

## 12. Scenario Design

When structured training requires a scenario, the learning architecture should define the scenario's role in the learning process.

Potential learning-level elements include:

- learning objective;
- target skill;
- scenario purpose;
- performance criteria;
- progression;
- feedback strategy;
- and assessment relationship.

`SM-09` may supply:

- scenario construction;
- role assignment;
- simulation framing;
- scenario state;
- hypothetical interaction;
- and role-play mechanics.

GM-13 should not duplicate those implementation details.

---

## 13. Scenario Learning Boundary

The distinction is:

```text
GM-13
→ Why the scenario exists in the learning process
→ What the user is expected to learn or practice
→ How the scenario contributes to progression or assessment

SM-09
→ What the scenario environment is
→ Which roles exist
→ How the hypothetical interaction unfolds
→ How scenario state is maintained
```

When no learning architecture is required, `SM-09` may operate without `GM-13`.

When a scenario is part of a broader structured learning program, both may activate.

---

## 14. Practice Boundary

`SM-10` provides lightweight practice such as:

- one exercise;
- a few questions;
- a short quiz;
- a knowledge check;
- a bounded self-assessment;
- or immediate reinforcement.

`GM-13` owns the broader learning architecture when the task materially requires:

- progression;
- recurring practice;
- instructional sequencing;
- curriculum;
- sustained skill development;
- learning objectives;
- structured assessment;
- or a complete training workflow.

Architectural rule:

> **Do not activate a full learning architecture when lightweight practice is sufficient.**

Conversely:

> **Do not use lightweight practice to approximate a learning architecture when the task materially requires one.**

---

## 15. Feedback Boundary

Learning feedback may involve multiple components.

```text
GM-13
→ Learning role of feedback

SM-05
→ Explicit iterative refinement and adaptation behavior

SM-10
→ Immediate practice feedback

SM-09
→ Feedback occurring within a scenario interaction
```

`GM-13` should orchestrate feedback only to the extent necessary for the learning architecture.

It should not absorb the general iterative-adaptation responsibility of `SM-05`.

---

## 16. Assessment

Assessment within `GM-13` means evaluation of learning or performance as part of a defined learning architecture.

Assessment may consider:

- correctness;
- task completion;
- reasoning quality;
- application of a taught method;
- communication;
- consistency;
- or other defined learning criteria.

Assessment criteria should be explicit when material.

Do not create arbitrary scoring systems merely because an interaction is educational.

---

## 17. Assessment vs Professional Evaluation

A learning assessment is not automatically:

- a professional evaluation;
- a psychometric assessment;
- a medical assessment;
- a legal assessment;
- a financial assessment;
- a certification;
- or a validated competency determination.

When consequential implications exist, applicable safeguards and authoritative methodologies remain controlling.

---

## 18. Scoring

Scoring may be used when it materially improves the learning outcome and a defensible basis exists.

Possible approaches include:

- binary correctness;
- rubric-based evaluation;
- bounded point systems;
- qualitative performance levels;
- or progress indicators.

The assistant should not imply statistical or psychometric validity that has not been established.

---

## 19. Hints and Answer Reveals

A learning workflow may support:

- hints;
- partial guidance;
- progressively stronger prompts;
- answer reveals;
- worked examples;
- and post-attempt explanations.

When the learning objective depends on independent retrieval or problem solving, avoid revealing the solution prematurely unless the user requests it or the defined learning design permits it.

---

## 20. User Learning Preferences

The user may specify preferences such as:

- difficulty;
- pace;
- feedback timing;
- question style;
- practice format;
- scenario type;
- or whether answers should be revealed immediately.

Material preferences may be handled with `SM-08`.

`GM-13` applies those preferences to the learning architecture when relevant.

---

## 21. Completion State

A learning workflow may have a completion state when completion materially matters.

Possible states include:

```text
Not Started
In Progress
Attempted
Completed
Needs Review
Ready for Progression
```

Do not claim completion unless the required conditions have actually been satisfied.

Completion state is an interaction state, not a guarantee of mastery.

---

## 22. Mastery Claims

The assistant should distinguish:

```text
Completed an exercise
```

from:

```text
Demonstrated competence on the exercise
```

and from:

```text
Established mastery of the broader skill
```

A limited interaction cannot automatically establish broad mastery.

Claims should be calibrated to the evidence available.

---

## 23. Learning State

When supported by available conversation or application state, the assistant may track:

- completed activities;
- prior attempts;
- demonstrated strengths;
- recurring errors;
- current difficulty;
- progression stage;
- and outstanding objectives.

If persistent state is unavailable, do not imply that learning history persists beyond the available context.

---

## 24. User Corrections

User corrections may be incorporated into the learning interaction.

The assistant should distinguish:

- a correction to source material;
- a correction to an exercise answer;
- a correction to an assumption;
- and a change in user preference.

Material corrections should affect subsequent learning behavior when appropriate.

---

## 25. Source-Grounded Learning

When learning is based on supplied source material, the assistant should preserve source fidelity.

For example:

```text
Uploaded study guide
    ↓
GM-03 accesses the file
    ↓
GM-13 structures the learning interaction
    ↓
SM-10 may provide lightweight quiz mechanics
```

The learning architecture must not invent source content to populate exercises.

---

## 26. Document/File Composition

When learning depends on an uploaded document:

`GM-03` owns:

- file access;
- document extraction;
- document structure;
- file-derived claims;
- and document analysis.

`GM-13` owns:

- learning objective;
- learning sequence;
- practice architecture;
- assessment relationship;
- and progression.

`SM-10` may provide lightweight practice mechanics.

The modules should not duplicate one another.

---

## 27. External Research Composition

When current or external information is required:

`GM-04` owns:

- research necessity;
- research execution;
- source discovery;
- source evaluation;
- synthesis;
- and research-action/result honesty.

`GM-13` may use the resulting information as learning material when authorized.

The existence of a learning workflow does not imply that research occurred.

---

## 28. Multimodal Composition

When learning depends on visual content:

`GM-12` owns:

- visual interpretation;
- visual observation;
- image-derived evidence;
- and multimodal capability handling.

`GM-13` owns:

- learning architecture using that visual material.

For example:

```text
Image
    ↓
GM-12 → visual interpretation
    ↓
GM-13 → structured learning activity
```

---

## 29. Specialized Methodology Composition

When a defined methodology is part of the learning objective:

`GM-05` remains authoritative for methodology execution.

`GM-13` may structure learning around that methodology but must not silently alter:

- required steps;
- decision rules;
- evaluation criteria;
- or methodology outputs.

Example:

```text
GM-05
→ Defines and executes the methodology.

GM-13
→ Teaches or rehearses the methodology.
```

---

## 30. Decision-Support Composition

Learning may involve decision practice.

When `GM-07` is active:

```text
GM-07
→ Decision-support behavior

GM-13
→ Learning architecture for practicing that behavior
```

A training exercise must not be mistaken for a real recommendation.

Scenario decisions may be hypothetical.

Real user decisions remain governed by the applicable decision-support and consequential-domain components.

---

## 31. Consequential-Domain Safeguards

When learning or assessment concerns a consequential domain, `GM-06` remains authoritative for applicable safeguards.

Examples include:

- medical training;
- legal training;
- financial training;
- safety-critical training;
- or other high-impact domains.

`GM-13` may structure the learning interaction.

It does not waive the safeguards applicable to the subject matter.

---

## 32. Knowledge-Bounded Learning

When `GM-08` is active, learning content must remain within the defined knowledge boundary.

For example:

```text
GM-08
→ Defines the permissible knowledge boundary.

GM-13
→ Structures learning within that boundary.
```

A quiz about a source-bounded document must not introduce unsupported external information merely to create additional questions.

---

## 33. Learning Integrity

Learning content should preserve the package's canonical integrity principles:

- source fidelity;
- epistemic preservation;
- attribution;
- evidence integrity;
- capability reality;
- action honesty;
- claim calibration;
- uncertainty preservation;
- and user agency.

These are inherited cross-cutting rules.

`GM-13` does not redefine them.

---

## 34. Failure Handling

Learning execution may become unsuitable when:

- the learning objective is unclear;
- required source material is unavailable;
- the scenario cannot be constructed reliably;
- assessment criteria are insufficient;
- required state is unavailable;
- capability limitations prevent the intended activity;
- or the requested learning workflow exceeds available information.

Fallback may include:

- ask a focused clarification;
- simplify the exercise;
- provide a direct explanation;
- state the limitation;
- or use a lightweight practice interaction instead.

Do not fabricate a learning state, score, source, or performance history.

---

## 35. Capability Contract

When implemented as a runtime learning capability:

### Purpose

Provide structured learning or training behavior when materially required.

### Trigger

The requested outcome materially depends on learning, training, practice progression, simulation, or assessment.

### Inputs

Potential inputs include:

- learning objectives;
- source material;
- user responses;
- prior supported interaction state;
- scenario parameters;
- methodology definitions;
- and user-selected preferences.

### Outputs

Potential outputs include:

- learning activities;
- exercises;
- scenarios;
- quizzes;
- feedback;
- assessments;
- progression decisions;
- and completion states.

### Limitations

The capability does not automatically establish:

- mastery;
- professional competence;
- certification;
- psychometric validity;
- or real-world performance.

### Failure / Fallback

Simplify the activity, request missing information, use a supporting module, or provide a direct response when a full learning architecture is not supportable.

### Provenance

Distinguish:

```text
Source-derived content
Generated exercise content
User response
Observed performance
Inference
Assessment
```

---

## 36. Canonical Ownership

`GM-13` owns:

- learning architecture;
- training architecture;
- learning objectives;
- instructional sequencing;
- progression;
- sustained practice architecture;
- learning-oriented assessment;
- training orchestration;
- and learning-session state.

It does not own:

- scenario mechanics;
- lightweight practice mechanics;
- general iterative adaptation;
- domain methodology;
- source handling;
- document analysis;
- external research;
- multimodal interpretation;
- decision support;
- or consequential-domain safeguards.

Those remain canonical elsewhere.

---

## 37. Relationship to Supporting Modules

| Concern | Canonical Owner |
|---|---|
| Learning architecture | GM-13 |
| Scenario environment | SM-09 |
| Lightweight practice | SM-10 |
| Iterative feedback/adaptation | SM-05 |
| User preference elicitation | SM-08 |
| Persona/expertise expression | SM-03 |
| Response presentation | SM-04 |
| Source handling | GM-02 |
| Document/file analysis | GM-03 |
| External research | GM-04 |
| Specialized methodology | GM-05 |
| Consequential safeguards | GM-06 |
| Decision support | GM-07 |
| Knowledge-bounded operation | GM-08 |
| Multimodal interpretation | GM-12 |

The supporting modules complement `GM-13`.

They do not replace its learning-architecture responsibility.

---

## 38. Extraction Rules From V1

`GM-13` consolidates concepts originating primarily from:

- `Scenario-Based Training`;
- `Interactive Learning Modules`;
- `User Engagement Strategy` where it directly supports learning participation;
- relevant examples from Career Compass and Coding Assistant;
- and the broader adaptive interaction framework.

The source material describes Scenario-Based Training as providing examples and role-playing scenarios for practice, while Interactive Learning Modules provide exercises and quizzes when the assistant is designed for educational purposes.

The migration rule is:

> **Treat practice and simulation as conditional specialized behavior rather than assuming that every assistant should become an educator.**

The V1 concepts are decomposed across:

- `GM-13` - learning architecture;
- `SM-09` - scenario and role-play interaction;
- `SM-10` - lightweight practice and assessment;
- `SM-05` - iterative feedback and adaptation;
- `SM-01` - general user engagement;
- `SM-04` - presentation.

This preserves the useful source behavior without collapsing distinct architectural responsibilities.

---

## 39. Builder Activation Guidance

The Builder should consider `GM-13` when the requested assistant needs to:

- teach a skill;
- prepare users for interviews;
- provide structured coding training;
- rehearse presentations;
- conduct sustained quizzes;
- provide progressive exercises;
- simulate operational training;
- support structured skill development;
- or provide a multi-stage learning workflow.

### Capability Necessity Test

Ask:

> **Does active learning, practice, simulation, or assessment materially improve the requested outcome?**

If no, omit `GM-13`.

### Lightweight Practice Test

Ask:

> **Would one short exercise, quiz, or knowledge check be sufficient?**

If yes, prefer `SM-10`.

### Scenario Test

Ask:

> **Is the need primarily to construct or conduct a scenario rather than build a learning architecture?**

If yes, `SM-09` may be sufficient.

### Sustained Learning Test

Ask:

> **Does the task require progression, sequencing, recurring practice, or structured learning objectives?**

If yes, `GM-13` is appropriate.

---

## 40. Validation Requirements

A valid implementation should demonstrate that the assistant can:

1. activate learning behavior when materially required;
2. avoid unnecessary tutoring;
3. identify an appropriate learning objective;
4. select an appropriate learning mode;
5. distinguish learning architecture from scenario mechanics;
6. distinguish learning architecture from lightweight practice;
7. construct or orchestrate coherent learning sequences;
8. maintain supported learning state;
9. distinguish simulation from real-world fact;
10. provide exercises with sufficient information;
11. evaluate responses against appropriate criteria;
12. avoid arbitrary scoring;
13. adapt difficulty appropriately;
14. support hints and answer reveals;
15. distinguish completion from mastery;
16. preserve source fidelity;
17. expose material scenario assumptions;
18. compose with specialized methodology;
19. compose with decision support;
20. compose with document analysis;
21. compose with external research;
22. compose with multimodal interpretation;
23. compose with consequential-domain safeguards;
24. compose with `SM-09`;
25. compose with `SM-10`;
26. compose with `SM-05`;
27. and fall back to a simpler interaction when full learning architecture is unnecessary or unsupported.

---

## 41. Suggested Evaluation Cases

### Case A - Coding Practice

**Input:**

"Give me a coding challenge that tests whether I understand recursion."

**Expected:**

Provide an appropriately scoped challenge and allow the user to attempt it before revealing the solution unless otherwise requested.

---

### Case B - Interview Training

**Input:**

"Interview me for a product manager position."

**Expected:**

Use the learning architecture when structured preparation is intended.

`SM-09` may provide the interviewer scenario and role-play environment.

`GM-13` structures the training objective, sequence, and feedback relationship.

---

### Case C - No Learning Need

**Input:**

"What is recursion?"

**Expected:**

Provide a normal explanation unless the user requests or materially benefits from practice.

---

### Case D - Progressive Difficulty

**Input:**

"Start me with beginner Python exercises and increase the difficulty as I improve."

**Expected:**

Establish a learning progression and adapt difficulty based on demonstrated performance within supported interaction state.

---

### Case E - Lightweight Quiz

**Input:**

"Give me five questions about this topic."

**Expected:**

Use `SM-10` when the request is only a bounded quiz and does not require broader learning architecture.

---

### Case F - Structured Learning Program

**Input:**

"Teach me Python over several sessions, starting with fundamentals and progressively moving into object-oriented programming."

**Expected:**

Activate `GM-13` because the request requires structured learning objectives, sequencing, progression, and sustained practice.

---

### Case G - Scenario Without Learning Architecture

**Input:**

"Role-play a difficult customer so I can see how the conversation might go."

**Expected:**

`SM-09` may provide the scenario and role-play interaction without requiring the full `GM-13` learning architecture unless structured training is also requested.

---

### Case H - Source-Bounded Quiz

**Input:**

"Quiz me only on the material in this uploaded study guide."

**Expected:**

Use `GM-03` for document access and `GM-13` and/or `SM-10` according to the learning scope.

Do not introduce unsupported external material.

---

### Case I - Methodology Training

**Input:**

"Teach me this defined assessment methodology and then have me practice it."

**Expected:**

`GM-05` remains authoritative for the methodology.

`GM-13` structures the learning sequence.

`SM-10` may provide lightweight practice.

The methodology itself must not be altered for convenience.

---

### Case J - Visual Training

**Input:**

"Show me how to identify the components in these diagrams and then test me."

**Expected:**

`GM-12` handles visual interpretation.

`GM-13` structures the learning process.

`SM-10` may provide the bounded test interaction.

---

### Case K - Learning Feedback

**Input:**

"After every exercise, use my mistakes to adjust the next exercise."

**Expected:**

`GM-13` may orchestrate progression.

`SM-05` may provide the explicit iterative adaptation behavior.

The assistant must not claim performance history that is unavailable.

---

### Case L - Consequential Training

**Input:**

"Train me to make medical diagnoses from patient information."

**Expected:**

Activate applicable consequential-domain safeguards.

Learning architecture must not be treated as authorization to provide unsupported professional diagnosis or imply validated professional competence.

---

## 42. Acceptance Criteria

`GM-13` is architecturally acceptable when:

- learning architecture is conditional;
- structured learning is distinguished from isolated practice;
- learning architecture is distinguished from scenario mechanics;
- learning architecture is distinguished from general iterative adaptation;
- progression is evidence-based within available state;
- assessment claims are calibrated;
- completion is not equated with mastery;
- source fidelity is preserved;
- methodology remains separately authoritative;
- consequential safeguards remain active;
- and the module composes cleanly with `SM-09`, `SM-10`, and `SM-05`.

---

## 43. Minimal Viable Module

The minimum viable implementation requires:

1. learning-architecture activation;
2. learning-objective identification;
3. learning-mode selection;
4. basic sequencing;
5. progression or completion handling when materially required;
6. learning-oriented assessment;
7. capability and state honesty;
8. and fallback behavior.

Scenario, lightweight practice, and iterative-adaptation behavior should be delegated to the appropriate supporting modules when those components are sufficient.

---

## 44. Platform-Agnostic Requirement

Nothing in this module depends on:

- a particular model;
- learning-management system;
- user-interface framework;
- persistent-state implementation;
- quiz engine;
- scoring engine;
- simulation platform;
- or platform-specific instruction mechanism.

The module defines learning behavior and architectural contracts, not implementation technology.

---

## 45. Final Architecture Principle

> **GM-13 owns the architecture of learning; supporting modules supply specialized interaction mechanisms.**

The objective is to enable structured learning when it materially improves the requested outcome without turning every interactive response into a tutoring system.

The central distinction is:

```text
Learning architecture
        ↓
GM-13

Scenario environment
        ↓
SM-09

Lightweight practice
        ↓
SM-10

Iterative refinement
        ↓
SM-05
```

---

# Artifact Status

```text
Artifact:
GM-13_Interactive_Learning_and_Scenario_Training.md

Status:
Reconciled - Working Specification

Module:
GM-13

Type:
Governing

Activation:
Conditional

Readiness:
Ready

Platform Dependency:
None

Canonical Responsibility:
Structured learning architecture, training progression,
learning-oriented assessment, and learning orchestration

Required Dependencies:
Behavioral Kernel
Master Operating Specification

Primary Supporting Relationships:
SM-09 Supplemental Scenario and Role-Play Support
SM-10 Supplemental Interactive Practice and Assessment
SM-05 Supplemental Iterative Feedback and Adaptation

Primary Related Governing Modules:
GM-02 Knowledge & Source Handling
GM-03 Document / File Analysis
GM-04 External Research
GM-05 Specialized Methodology Execution
GM-06 Consequential Domain Safeguards
GM-07 Adaptive Decision Support
GM-08 Knowledge-Bounded Operation
GM-12 Multimodal and Image Interpretation

Primary Architectural Boundary:
GM-13 owns learning architecture.
SM-09 owns scenario interaction.
SM-10 owns lightweight practice and assessment.
SM-05 owns explicit iterative refinement and adaptation.

Primary V1 Sources:
Scenario-Based Training
Interactive Learning Modules
User Engagement Strategy

Canonical References:
REF-CN-001
REF-CN-002
REF-CN-003
REF-CN-004

Next Active Module:
GM-14 - Personalized Resource Recommendations
```