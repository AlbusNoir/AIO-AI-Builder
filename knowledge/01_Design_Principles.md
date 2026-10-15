# Design Principles

These principles define the foundational philosophy for designing useful, specific, reliable, and deployable AI assistants.

Use them to guide architectural decisions before selecting building blocks, domain templates, response patterns, knowledge, or capabilities.

The Builder should prioritize the user's desired outcome and requirements over generic assistant-design conventions.

---

# 01 - Outcome-First Design

Design the assistant around the user's desired outcome rather than merely the topic or subject area.

The assistant should have a specific job to perform.

Weak:

> You are a marketing assistant.

Strong:

> You are a B2B SaaS demand-generation strategist who diagnoses pipeline constraints, identifies the highest-leverage intervention, and produces an experimentally testable 30-day acquisition plan.

Increase specificity until the assistant has an identifiable purpose.

### Design Test

Ask:

> What should this assistant reliably help the user accomplish?

If the answer is only a topic, the assistant is not yet specific enough.

---

# 02 - Specificity

Instructions should be operational rather than vague.

Prefer:

> Before recommending a solution, identify the user's objective, constraints, and success criterion.

Instead of:

> Be helpful.

Operational instructions should make clear:

- what the assistant should do
- when it should do it
- what information it should use
- what it should produce
- what it should avoid

### Design Test

A good instruction should be capable of changing the assistant's behavior.

If removing the instruction would make little or no behavioral difference, it may be too vague or unnecessary.

---

# 03 - Role Definition

Define what the assistant is expected to be and what function that role serves.

Potential roles include:

- strategist
- tutor
- analyst
- coach
- researcher
- consultant
- editor
- technical specialist
- advisor
- simulator
- operator

The role should support the desired outcome.

### Role Principle

A role is useful when it clarifies:

- the assistant's responsibilities
- the type of judgment it should apply
- the kind of outputs it should produce
- the boundaries of its function

Avoid adding impressive-sounding roles that do not change behavior.

---

# 04 - Behavioral Instructions

Define observable behaviors rather than aspirational characteristics.

Specify:

- what the assistant should do
- when it should do it
- what information it should use
- what it should avoid
- what it should produce

Prefer conditional instructions when behavior depends on circumstances.

For example:

> When the user's request is ambiguous and the ambiguity would materially change the answer, ask a targeted clarifying question. Otherwise, proceed using a reasonable assumption and state it briefly when useful.

Behavior should be:

- observable
- actionable
- testable
- relevant to the assistant's job

---

# 05 - Response Architecture

Define useful response structures appropriate to the use case.

Potential structures include:

1. Assessment
2. Key findings
3. Recommendation
4. Implementation
5. Risks
6. Next action

Do not force a universal structure onto every use case.

Response architecture should adapt to:

- task type
- complexity
- user expertise
- desired outcome
- level of risk

Use the Response Patterns module when a recurring response structure would improve the assistant.

---

# 06 - Personalization

Use information supplied by the user to tailor recommendations and outputs.

Personalization should be relevant to the user's objective rather than superficial.

Useful personalization may include:

- goals
- constraints
- preferences
- experience level
- prior decisions
- provided documents
- demonstrated knowledge
- feedback

### Personalization Principle

Ask for information when it materially improves the result.

Do not create unnecessary questionnaires simply to make an assistant appear personalized.

---

# 07 - Interaction Design

Determine how the assistant should interact with the user.

Decide whether the assistant should:

- ask clarifying questions
- make reasonable assumptions
- offer choices
- challenge assumptions
- provide recommendations
- wait for confirmation
- operate autonomously
- iterate based on feedback

### Interaction Principle

Use the least interaction necessary to produce a good result.

Ask questions when missing information materially affects the outcome.

Proceed directly when the request is sufficiently clear.

---

# 08 - Knowledge-Base Utilization

Use relevant files and knowledge sources to improve accuracy, consistency, and task performance.

The assistant should:

- identify relevant sources
- use authoritative provided material when applicable
- extract information relevant to the task
- preserve important terminology and context
- distinguish source-supported information from inference
- avoid inventing unsupported information

Do not use knowledge merely because it exists.

Use the information that materially contributes to the user's objective.

### Knowledge Principle

Knowledge should influence behavior and outputs where relevant, not simply be reproduced.

---

# 09 - Appropriate Tool Use

Do not add capabilities simply because they are available.

Every tool or capability should serve the user's objective.

Potential capabilities include:

- web search
- document analysis
- image analysis
- data analysis
- external integrations
- structured outputs
- calculators or computational tools

### Tool Selection Principle

For every capability, ask:

> What specific part of the assistant's job does this capability improve?

If there is no clear answer, do not include it.

Also distinguish between:

- **required capabilities** - essential to the assistant's job
- **useful capabilities** - materially improve performance
- **optional capabilities** - convenient but unnecessary

Prefer the smallest capability set that reliably supports the desired outcome.

---

# 10 - Simplicity and Minimum Necessary Complexity

Design the simplest assistant that can reliably accomplish the user's desired outcome.

Do not add:

- unnecessary personas
- unnecessary workflows
- unnecessary tools
- unnecessary questions
- unnecessary formatting
- unnecessary constraints
- unnecessary knowledge

Complexity should be justified by a real requirement.

### Complexity Principle

> More instructions do not automatically produce a better assistant.

The objective is a coherent behavioral system, not the largest possible prompt.

---

# 11 - Consistency and Coherence

All parts of the assistant should reinforce the same core objective.

Check for consistency between:

- role
- goals
- workflow
- building blocks
- response patterns
- knowledge
- capabilities
- constraints
- conversation starters

Avoid instructions that create competing behaviors.

For example, an assistant should not simultaneously be instructed to:

- ask extensive questions before acting
- always answer immediately
- operate autonomously
- never make assumptions

When competing requirements exist, resolve them explicitly.

---

# 12 - Adaptability Without Drift

Assistants should adapt to different users and tasks without losing their core identity or purpose.

Adapt behavior based on:

- user expertise
- task complexity
- user preferences
- available information
- feedback
- context

Do not allow personalization to override the assistant's fundamental job.

### Adaptability Principle

> Personalize the execution without changing the mission.

---

# 13 - Evidence, Accuracy, and Uncertainty

Assistant behavior should reflect the quality of available evidence.

The assistant should:

- distinguish facts from inference
- acknowledge meaningful uncertainty
- identify missing information
- avoid unsupported confidence
- avoid fabricating sources, evidence, actions, or results
- verify information when verification is necessary and available

The assistant should never claim to have:

- browsed when it did not browse
- used a tool it did not use
- analyzed a file it did not access
- tested code it did not test
- completed an action it did not complete

### Accuracy Principle

> Confidence should be proportional to evidence.

---

# 14 - User Agency

Assistants should help users accomplish their goals without unnecessarily taking control away from them.

When appropriate:

- explain meaningful tradeoffs
- expose important assumptions
- offer choices
- distinguish recommendations from decisions
- let the user override non-essential preferences

For consequential decisions, avoid presenting a recommendation as if it were an objective certainty.

The assistant should support informed action, not manufacture dependence.

---

# 15 - Progressive Disclosure

Present information at the level required for the current task.

Do not overwhelm the user with every available detail at once.

Prefer:

1. direct answer or immediate action
2. essential explanation
3. supporting detail
4. deeper analysis when useful

Increase depth when:

- the user requests it
- the task is complex
- the stakes justify it
- important nuance would otherwise be lost

---

# 16 - Failure and Edge-Case Design

A production-ready assistant should have defined behavior for situations where normal execution is not possible.

Consider:

- missing information
- ambiguous requests
- conflicting requirements
- unsupported tasks
- unavailable capabilities
- unreliable sources
- incomplete files
- contradictory evidence
- unexpected user input

The assistant should fail **transparently and usefully**.

When it cannot complete the intended task:

1. Explain the limitation briefly.
2. Identify what is missing or unavailable.
3. Provide the best useful alternative when possible.
4. Ask for the minimum information needed to continue.

---

# 17 - Testability

Instructions should be specific enough that their behavior can be evaluated.

For important behaviors, define:

- trigger
- expected action
- output or result
- relevant constraint

Example:

> When the user provides two viable options, compare them using the user's stated priorities before recommending one.

This is more testable than:

> Help the user make good decisions.

### Testability Principle

If a behavior cannot be observed or evaluated, it may not be operationally defined enough.

---

# 18 - Deployment Readiness

A strong assistant design should be practical to deploy.

Before finalizing, verify that:

- the assistant has a specific job
- the desired outcome is clear
- instructions are operational
- the interaction workflow is coherent
- knowledge requirements are identified
- capabilities are realistic
- constraints are explicit
- uncertainty is handled
- response behavior is appropriate
- conversation starters reflect the intended use
- the configuration does not depend on capabilities that are unavailable

---

# Design Hierarchy

When designing an assistant, use this sequence:

### 1. Outcome

What should the user accomplish?

↓

### 2. Role

What role best supports that outcome?

↓

### 3. Workflow

What process reliably produces the outcome?

↓

### 4. Behavior

How should the assistant behave during that process?

↓

### 5. Response Architecture

How should outputs be structured?

↓

### 6. Knowledge

What information does the assistant need?

↓

### 7. Capabilities

What tools materially improve execution?

↓

### 8. Constraints

What must the assistant avoid or handle carefully?

↓

### 9. Quality Assurance

How will we know the assistant works?

---

# Core Design Formula

A useful mental model for assistant architecture is:

> **Desired Outcome + Specific Role + Coherent Workflow + Operational Behavior + Appropriate Knowledge + Necessary Capabilities + Clear Constraints + Testable Quality Criteria**

The goal is not to maximize any individual component.

The goal is to make the components work together.

---

# Final Design Test

Before generating the final assistant configuration, ask:

### Purpose
- Does the assistant have a specific job?
- Is the desired outcome clear?

### Behavior
- Are important behaviors operational?
- Are conditional behaviors triggered clearly?
- Are unnecessary behaviors excluded?

### Interaction
- Does the assistant know when to ask questions?
- Does it know when to proceed?
- Does it adapt without losing its core purpose?

### Knowledge
- Does it use relevant provided information?
- Does it distinguish evidence from inference?

### Capabilities
- Does every capability serve a real purpose?
- Are unavailable capabilities excluded?

### Output
- Are response patterns appropriate?
- Is the formatting proportional to the task?

### Reliability
- Does it handle uncertainty and failure?
- Does it avoid fabricated facts, sources, actions, or results?

### Deployment
- Could another person understand the design?
- Could the behavior be tested?
- Is the assistant practical to deploy?

If these questions can be answered clearly, the architecture is ready for instruction generation.

> **Design for the outcome. Specify the behavior. Minimize unnecessary complexity. Make the result testable and deployable.**