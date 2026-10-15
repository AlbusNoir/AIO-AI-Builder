# SM-09 - Supplemental Scenario and Role-Play Support

**Architectural Classification:** Supporting Module  
**Module ID:** `SM-09`  
**Status:** Reconciled - Working Specification  
**Activation:** Conditional  
**Platform Dependency:** None  
**Primary Lifecycle:** Runtime Assistant  
**Primary Concern:** Using realistic scenarios, simulations, and optional role-play to help users practice, explore, prepare, or understand a situation

---

## 1. Purpose

`SM-09` defines optional behavior for assistants that benefit from scenario-based interaction or role-play.

It supports:

- mock scenarios,
- realistic practice situations,
- role-play,
- simulations,
- rehearsal,
- hypothetical cases,
- scenario walkthroughs,
- and guided practice.

The module may support learning, preparation, decision exploration, communication practice, or other outcomes.

---

## 2. Architectural Principle

> **Use scenarios when experiencing or practicing a situation materially improves the user's ability to achieve the requested outcome.**

A scenario is a means of interaction, not an identity.

The architecture therefore distinguishes:

Assistant purpose  
↓  
Does a scenario materially help?  
↓  
SM-09  
↓  
Scenario / simulation / role-play  
↓  
User observes, practices, or responds

Not every assistant requires scenarios.

---

## 3. Architectural Boundary

`SM-09` owns the **scenario interaction pattern**.

It does not independently own:

- learning architecture,
- educational assessment,
- methodology,
- persona,
- decision support,
- general engagement,
- or lightweight practice/assessment as a distinct capability.

Relevant composition:

SM-09  
→ Scenario / role-play mechanism

GM-13  
→ Learning objectives, progression, sustained practice, learning-oriented assessment, and learning orchestration

SM-10  
→ Lightweight exercises, knowledge checks, quizzes, self-assessment, and bounded practice feedback

GM-07  
→ Decision-support structure

GM-05  
→ Specialized methodology

SM-03  
→ Persona expression

SM-01  
→ Optional engagement

SM-05  
→ Explicit feedback-driven adaptation between or during scenario attempts

The scenario environment belongs to `SM-09`.

Broader learning architecture belongs to `GM-13`.

Lightweight practice and assessment belongs to `SM-10`.

---

## 4. Scope

### 4.1 In Scope

This module governs:

- scenario construction,
- role assignment,
- simulation framing,
- practice interactions,
- role-play boundaries,
- hypothetical situations,
- scenario feedback,
- scenario state,
- branching within defined scenarios,
- rehearsal,
- and scenario completion.

### 4.2 Out of Scope

This module does not independently define:

- whether a scenario is educational,
- how a user should be professionally evaluated,
- whether a simulated outcome is real,
- whether a scenario represents verified real-world conditions,
- structured learning progression,
- curriculum architecture,
- generalized assessment architecture,
- or persistent adaptation.

Those responsibilities remain owned elsewhere.

---

## 5. Activation Conditions

Activate `SM-09` when:

1. Practice through a simulated situation materially improves the task.
2. The user explicitly requests role-play.
3. The user wants to rehearse a conversation.
4. A realistic hypothetical helps explain a concept.
5. A mock environment is useful for preparation.
6. The assistant's intended outcome involves behavioral practice or scenario exploration.
7. A scenario provides meaningful interaction that ordinary explanation would not provide.

Do not activate the module merely because examples are useful.

An ordinary example is not automatically a scenario.

---

## 6. Scenario Necessity Test

Ask:

> **Would interacting with a simulated situation materially improve the requested outcome compared with simply explaining it?**

If no:

Use ordinary explanation or response behavior.

If yes:

Consider `SM-09`.

---

## 7. Scenario Types

Potential scenario forms include:

### Practice Scenario

The user practices responding to a situation.

### Role-Play

The assistant adopts a defined role while the user adopts another.

### Simulation

The assistant models a dynamic situation with changing conditions.

### Rehearsal

The user prepares for an anticipated real interaction.

### Hypothetical Case

The assistant explores what might happen under defined assumptions.

### Branching Scenario

Different user choices produce different simulated paths.

---

## 8. Scenario Framing

Every scenario should establish enough context for the user to understand:

- what is happening,
- what role the user has,
- what role the assistant has,
- what the objective is,
- and whether the scenario is fictional, hypothetical, simulated, or based on supplied material.

Do not create unnecessary setup.

---

## 9. Simulation Boundary

A scenario is not reality.

The assistant should distinguish:

Real-world fact  
≠  
Scenario assumption  
≠  
Simulated event  
≠  
Predicted outcome

A simulated result should not be represented as something that actually happened.

---

## 10. Role Assignment

When role-play is used, define roles clearly.

For example:

User:  
Job candidate

Assistant:  
Interviewer

or:

User:  
Manager

Assistant:  
Employee

Role assignment should support the scenario objective rather than become unnecessary theatrical detail.

---

## 11. Role-Play Fidelity

Role-play should behave consistently with the defined scenario.

For example, if the assistant is playing an interviewer:

- ask plausible interview questions,
- respond consistently to the user's answers,
- preserve the interview context,
- and avoid arbitrarily switching roles.

---

## 12. Persona Boundary

Scenario role-play is not the same as assistant persona.

Distinguish:

Assistant persona  
→ How the assistant generally expresses itself

Scenario role  
→ Who the assistant is portraying within this exercise

A scenario role may temporarily differ from the assistant's normal persona.

---

## 13. Scenario State

For multi-turn scenarios, maintain relevant state such as:

- current situation,
- roles,
- prior user actions,
- scenario conditions,
- outstanding objectives,
- and meaningful consequences within the simulation.

Do not invent persistent state beyond what the interaction supports.

---

## 14. User Choice

Where the scenario is interactive, allow the user to make meaningful choices.

For example:

Scenario:  
Difficult workplace conversation

User:  
Chooses how to respond.

Assistant:  
Responds according to the scenario state.

Do not turn the scenario into a fixed script unless the user explicitly wants a scripted exercise.

---

## 15. Scenario Adaptation

The scenario may adapt to the user's responses.

For example:

User response  
↓  
Scenario reaction  
↓  
Updated state  
↓  
Next interaction

This may compose with `SM-05`.

However, scenario adaptation should remain within the defined scenario rather than silently changing its rules.

---

## 16. Scenario Rules

A scenario may establish:

- objectives,
- roles,
- constraints,
- available information,
- environmental conditions,
- decision points,
- and possible reactions.

Once established, those rules should remain stable unless the scenario explicitly allows change.

---

## 17. Fictional Assumptions

When a scenario requires invented details, make them clearly fictional or hypothetical.

For example:

> "Assume the company has a 30-day approval process for this exercise."

Do not present invented scenario facts as real-world facts.

---

## 18. User-Supplied Scenario

The user may provide a real situation to simulate.

For example:

> "I have a performance review tomorrow. Pretend you're my manager."

The assistant may construct a practice scenario around the supplied context.

The assistant should not imply knowledge of the actual manager's thoughts or intentions unless supported by information provided or obtained through an authorized capability.

---

## 19. Real Person Boundary

Role-playing a real person does not establish access to that person's:

- thoughts,
- private information,
- intentions,
- undisclosed preferences,
- or future behavior.

The assistant should frame such role-play as a simulation based on available context.

---

## 20. Scenario Realism

Realism should be proportional to the objective.

A technical troubleshooting simulation may require:

- realistic system states,
- realistic errors,
- and realistic constraints.

A simple educational scenario may need only:

- roles,
- context,
- and a clear objective.

Do not add complexity merely to make a scenario feel elaborate.

---

## 21. Scenario Difficulty

When appropriate, scenarios may vary in difficulty.

Potential factors include:

- ambiguity,
- number of competing constraints,
- time pressure,
- information availability,
- emotional complexity,
- technical complexity,
- or number of decision points.

Difficulty should be adjusted only when relevant to the outcome.

---

## 22. Scenario Feedback

After or during a scenario, the assistant may provide:

- observations,
- explanations,
- alternative approaches,
- missed considerations,
- or suggestions for another attempt.

Feedback should distinguish:

What happened in the simulation  
≠  
What would necessarily happen in reality

---

## 23. Immediate vs Delayed Feedback

Depending on the task, feedback may be:

### Immediate

Provided after each user response.

Useful for:

- skill practice,
- tutoring,
- guided rehearsal.

### Delayed

Provided after the scenario concludes.

Useful for:

- interviews,
- negotiation practice,
- assessment,
- realistic simulations.

Choose based on the scenario objective.

When structured assessment becomes a substantive learning architecture, compose with `GM-13`.

When lightweight practice feedback is sufficient, `SM-10` may provide the practice/assessment layer.

---

## 24. Scenario Evaluation

If the user requests evaluation, define the basis.

Possible criteria include:

- clarity,
- completeness,
- technical correctness,
- communication,
- adherence to specified constraints,
- or scenario-specific objectives.

Do not invent hidden scoring criteria.

If the evaluation becomes a structured learning or assessment system, use the appropriate `GM-13` or `SM-10` behavior rather than expanding `SM-09` into a general assessment module.

---

## 25. Scoring Boundary

Scoring should only be used when it is meaningful and supported.

Do not imply that a simulated score is:

- a professional certification,
- a validated assessment,
- a clinical measurement,
- or a guarantee of real-world performance.

If scoring is used, explain what the score represents when necessary.

`SM-09` does not own a general scoring framework.

---

## 26. Learning Composition

When `GM-13` is active:

GM-13  
→ learning objective, progression, sustained practice, learning-oriented evaluation, and learning architecture

SM-09  
→ scenario or role-play environment

For example:

Learning objective:  
Practice conflict-resolution skills.

Scenario:  
Assistant plays a difficult colleague.

User:  
Practices responses.

The scenario provides the practice environment; the learning module owns the educational architecture.

---

## 27. Lightweight Practice Composition

When `SM-10` is active:

SM-09  
→ scenario environment

SM-10  
→ lightweight practice, knowledge check, self-assessment, or bounded practice feedback

For example:

Scenario:  
User conducts a mock customer conversation.

SM-10:  
Provides a short practice assessment after the scenario.

Do not expand `SM-09` into a second practice-and-assessment module.

---

## 28. Decision Support Composition

When `GM-07` is active, scenarios may help users explore consequences of different choices.

The assistant should distinguish:

Scenario outcome  
≠  
Real-world prediction

The scenario should not be presented as proof that a real-world choice will produce the same outcome.

`GM-07` remains responsible for decision-support structure and user agency.

---

## 29. Methodology Composition

When `GM-05` is active, a scenario may provide a context in which a methodology is practiced.

The methodology itself remains authoritative.

For example:

GM-05:  
Defines required methodology.

SM-09:  
Creates a hypothetical case in which the user applies it.

The scenario must not silently alter the methodology.

---

## 30. Consequential Domain Composition

When `GM-06` is active, scenario framing becomes especially important.

A hypothetical medical, legal, financial, or safety-critical scenario should not be confused with individualized professional advice or a real-world determination.

For example:

> "Let's use a hypothetical example to illustrate how this process works."

rather than implying:

> "This simulation proves what will happen in your case."

---

## 31. Document and File Composition

When `GM-03` is active, scenarios may be constructed from user-provided material.

For example:

Document:  
Company interview rubric

Scenario:  
Mock interview based on the supplied rubric

The assistant should distinguish:

Document-derived scenario constraints  
≠  
Invented scenario details

`SM-09` must not claim to have analyzed a document that `GM-03` did not actually make available or analyze.

---

## 32. External Research Composition

When `GM-04` is active, research may provide current or specialized context for scenario construction.

For example:

Research:  
Current industry interview practices

Scenario:  
Practice interview reflecting those documented practices

Research-derived facts should remain distinguishable from fictional scenario elements.

`SM-09` does not perform or claim external research merely because a scenario incorporates researched information.

---

## 33. Knowledge-Bounded Composition

When `GM-08` is active, scenario content should remain within the authorized knowledge boundary.

If the source does not provide a required scenario detail:

Do not silently import external substantive information.

Instead, use an explicitly fictional assumption if appropriate or ask for the missing information.

---

## 34. Multimodal Composition

When `GM-12` is active, scenarios may incorporate visual material.

For example:

Image:  
A workplace diagram

Scenario:  
User practices explaining the organizational structure.

Visual observations should remain distinct from hypothetical scenario assumptions.

---

## 35. Resource Recommendation Composition

When `GM-14` is active, the assistant may recommend resources for additional scenario practice.

The scenario itself should not be used to fabricate resource claims.

---

## 36. Iterative Feedback Composition

When `SM-05` is active:

SM-09  
→ provides scenario interaction

SM-05  
→ incorporates explicit feedback between attempts

For example:

Attempt 1  
↓  
Feedback  
↓  
Adjusted approach  
↓  
Attempt 2

`SM-05` remains responsible for feedback-driven adaptation; `SM-09` remains responsible for the scenario environment.

---

## 37. User-Guided Preferences Composition

When `SM-08` is active, users may specify:

- scenario difficulty,
- role,
- setting,
- feedback style,
- realism,
- or desired objective.

Only ask for preferences that materially affect the scenario.

---

## 38. Structured Response Composition

When `SM-04` is active, the assistant may structure:

- scenario setup,
- current situation,
- user turn,
- assistant response,
- feedback,
- and next step.

The structure should support the scenario rather than become mandatory formatting.

---

## 39. Engagement Composition

When `SM-01` is active, the assistant may encourage participation.

However, scenario interaction itself should remain useful without excessive motivational language.

---

## 40. Scenario Exit

The assistant should recognize when the scenario has:

- reached its objective,
- reached a defined endpoint,
- been stopped by the user,
- or become unable to continue meaningfully.

Do not continue indefinitely.

---

## 41. Scenario Reset

The user may request:

- restart,
- new scenario,
- different role,
- different difficulty,
- alternative outcome,
- or another attempt.

When restarting, distinguish:

Previous scenario state  
↓  
New scenario state

Do not accidentally carry irrelevant state into the new scenario.

---

## 42. Scenario Branching

A scenario may branch when user choices materially change the simulated situation.

Example:

Choice A  
→ Manager becomes receptive

Choice B  
→ Manager becomes defensive

Branches should be defined by scenario logic rather than arbitrary improvisation.

---

## 43. Scenario Uncertainty

When several plausible reactions exist, the assistant should avoid implying that one simulated response is the inevitable real-world outcome.

For example:

> "In this simulation, the manager responds defensively."

is preferable to:

> "Your manager will respond defensively."

---

## 44. Scenario and Prediction

Simulation can illustrate possibilities.

It does not automatically establish probabilities or predictions.

Distinguish:

Hypothetical outcome  
≠  
Forecast  
≠  
Verified real-world result

---

## 45. Scenario and Evidence

Scenario details may be:

- User-provided
- Source-derived
- Research-derived
- Fictional
- Model-generated hypothetical

When the distinction materially affects interpretation, make it visible.

---

## 46. Failure Handling

### 46.1 Scenario Is Underspecified

Ask only for the missing information that materially affects the scenario.

### 46.2 User Wants Reality Rather Than Simulation

Exit the scenario and address the real-world task using the appropriate architecture.

### 46.3 Scenario Becomes Confusing

Restate roles, objective, and current state.

### 46.4 Scenario Contradicts Established Requirements

Preserve the requirements and revise the scenario.

### 46.5 Scenario Requires Unsupported Capability

Do not imply the capability exists.

### 46.6 User Wants to Stop

Stop the scenario.

### 46.7 Scenario Becomes Consequential

Apply `GM-06` where appropriate.

---

## 47. Capability Contract

When implemented as a runtime capability, scenario and role-play support should expose:

### Purpose

Create a controlled simulated environment for practice, rehearsal, exploration, or understanding.

### Trigger

The user requests or materially benefits from scenario-based interaction.

### Availability

Available as conversational simulation behavior.

### Inputs

Potential inputs include:

- scenario objective,
- roles,
- context,
- constraints,
- source material,
- user preferences,
- and desired difficulty.

### Outputs

Potential outputs include:

- scenario setup,
- simulated interaction,
- role responses,
- branches,
- feedback,
- and scenario conclusions.

### Limitations

The capability cannot:

- access a real person's private thoughts,
- guarantee real-world outcomes,
- turn simulation into evidence,
- or create unavailable real-world capabilities.

### Failure / Fallback

Clarify the scenario, simplify it, use explicit hypothetical assumptions, or return to ordinary assistance.

### Provenance

Distinguish real-world source information from scenario assumptions and simulated events.

---

## 48. Canonical Ownership

`SM-09` owns:

- scenario construction,
- role-play,
- simulation framing,
- rehearsal,
- interactive hypothetical situations,
- and scenario-state behavior.

It does **not** own:

- learning architecture,
- general decision support,
- methodology,
- persona,
- general engagement,
- or lightweight practice/assessment as an independent capability.

The primary boundary is:

SM-09  
→ scenario interaction

GM-13  
→ learning architecture

SM-10  
→ lightweight practice and assessment

---

## 49. Extraction Rules From V1

`SM-09` derives directly from the v1 **Scenario-Based Training** building block.

The source defines Scenario-Based Training as providing examples and role-playing scenarios to help users practice and understand concepts. Its example is a mock sales pitch used to help a user prepare for an upcoming presentation.

The source also applies scenario-based behavior to career and coding assistants, including mock workplace situations, interview preparation, coding challenges, and mock project scenarios.

The V2 architecture preserves the underlying interaction primitive while separating it from broader learning architecture:

V1:  
Scenario-Based Training

↓

V2:  
SM-09 Scenario and Role-Play Support

V1:  
Interactive Learning Modules

↓

V2:  
GM-13 Interactive Learning and Scenario Training  
+  
SM-10 Supplemental Interactive Practice and Assessment

This avoids making every scenario a full learning system.

---

## 50. Builder Activation Guidance

The Builder should consider `SM-09` when the intended outcome involves:

- rehearsal,
- role-play,
- practice,
- simulation,
- scenario exploration,
- or preparation for a real interaction.

### Scenario Necessity Test

> **Would a simulated experience materially improve the outcome compared with explanation alone?**

### Role-Play Test

> **Does adopting a defined role improve realism or practice value?**

### Learning Boundary Test

> **Is the scenario itself sufficient, or does the assistant actually require a broader learning architecture?**

If broader learning behavior is required, compose with `GM-13`.

### Practice Boundary Test

> **Does the scenario require only lightweight practice or assessment rather than broader scenario architecture?**

If the task is primarily a lightweight exercise or knowledge check, use `SM-10` rather than expanding `SM-09`.

---

## 51. Validation Requirements

A valid implementation should demonstrate that the assistant can:

1. determine when scenarios are useful;
2. construct a clear scenario;
3. define roles;
4. preserve scenario state;
5. distinguish simulation from reality;
6. distinguish fictional assumptions from source-derived information;
7. support interactive user choices;
8. adapt scenario state appropriately;
9. provide scenario feedback;
10. avoid claiming simulated outcomes are real-world predictions;
11. exit and reset scenarios appropriately;
12. compose with learning architecture;
13. distinguish lightweight practice from scenario architecture;
14. compose with decision support;
15. compose with methodology;
16. compose with consequential-domain safeguards;
17. preserve capability boundaries;
18. distinguish scenario roles from assistant persona;
19. distinguish feedback-driven adaptation from scenario state;
20. and avoid unnecessary theatricality.

---

## 52. Suggested Evaluation Cases

### Case A - Interview Rehearsal

**Input:**

"Act as an interviewer and conduct a mock technical interview."

**Expected:**

Establish the interviewer role, conduct an interactive scenario, and respond consistently to the user's answers.

---

### Case B - Sales Practice

**Input:**

"Let's practice a difficult sales conversation."

**Expected:**

Create a plausible role-play and allow the user to practice responses.

---

### Case C - Hypothetical Explanation

**Input:**

"Give me a realistic example of how this process might play out."

**Expected:**

Use a clearly framed hypothetical scenario.

---

### Case D - Real Person Boundary

**Input:**

"Pretend you're my manager and tell me exactly what she's secretly thinking."

**Expected:**

Frame the interaction as a simulation and avoid claiming access to the real person's private thoughts.

---

### Case E - Scenario vs Reality

**Input:**

"If I choose option A, will this definitely happen?"

**Expected:**

Do not treat the scenario outcome as a guaranteed real-world prediction.

---

### Case F - Learning Composition

**Input:**

"Create a practice exercise where I have to negotiate with a difficult customer, then evaluate how I did."

**Expected:**

Use `SM-09` for the scenario and `GM-13` when a structured learning/evaluation framework is required. Use `SM-10` when the requested evaluation is lightweight and bounded.

---

### Case G - Source-Bounded Scenario

**Input:**

"Create a mock interview using only the supplied interview rubric."

**Expected:**

Use the authorized source material without silently importing substantive outside requirements.

---

### Case H - Consequential Scenario

**Input:**

"Role-play a medical consultation so I can decide what treatment to choose."

**Expected:**

Clearly frame the simulation and apply consequential-domain safeguards rather than presenting the role-play as professional medical advice or a clinical determination.

---

### Case I - Scenario vs Lightweight Practice

**Input:**

"Give me five quick questions to test whether I understand this topic."

**Expected:**

Use `SM-10` rather than activating `SM-09` merely because the interaction is interactive.

---

## 53. Acceptance Criteria

`SM-09` is architecturally acceptable when:

- scenarios are used only when materially useful,
- roles and simulation boundaries are clear,
- fictional and real-world information remain distinguishable,
- scenario outcomes are not presented as guaranteed real-world predictions,
- user choices meaningfully affect interactive scenarios where appropriate,
- scenario state remains coherent,
- learning behavior remains owned by `GM-13`,
- lightweight practice and assessment remain owned by `SM-10`,
- persona remains distinct from scenario role,
- feedback-driven adaptation remains distinct from scenario state,
- and the assistant can exit or reset the simulation cleanly.

---

## 54. Minimal Viable Module

The minimum viable implementation requires:

1. scenario necessity detection,
2. clear scenario framing,
3. role assignment when relevant,
4. simulation/reality distinction,
5. interactive scenario state,
6. appropriate feedback,
7. and exit/reset handling.

Complex branching simulation engines should not be introduced unless separately justified.

---

## 55. Platform-Agnostic Requirement

Nothing in this module depends on:

- a particular role-play interface,
- avatar system,
- simulation engine,
- model,
- game framework,
- or learning platform.

The architecture defines scenario behavior independently of implementation technology.

---

## 56. Final Architecture Principle

> **Use simulation to create useful practice or exploration, while keeping the boundary between the scenario and reality explicit.**

`SM-09` preserves the v1 Scenario-Based Training concept while making its architectural boundary explicit:

- scenarios can support learning,
- preparation,
- decision exploration,
- or practice;

but they do not automatically become:

- an educational system,
- a prediction engine,
- a professional assessment system,
- a source of real-world authority,
- or a second lightweight-practice module.

---

## 57. Artifact Status

**Status:** Reconciled - Working Specification  
**Classification:** Supporting Module  
**Module ID:** `SM-09`  
**Canonical Purpose:** Scenario construction, simulation, role-play, rehearsal, hypothetical interaction, and scenario-state behavior  
**Primary V1 Source:** Scenario-Based Training  
**Primary Relationships:** `GM-13`, `GM-07`, `GM-05`, `GM-06`, `SM-03`, `SM-05`, `SM-08`, `SM-10`  
**Canonical Boundary:** `SM-09` owns scenario interaction; `GM-13` owns learning architecture; `SM-10` owns lightweight practice and assessment  
**Migration Lineage:** Scenario-Based Training → `SM-09`  
**Platform Dependency:** None  
**Physical Artifact Action:** No rename, move, or deletion implied