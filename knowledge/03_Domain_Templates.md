# Domain Templates

Use these as starting architectures for recognizable assistant domains.

A Domain Template is a reusable workflow pattern that helps the Builder establish an appropriate starting architecture for a use case.

Domain Templates are not mandatory workflows. Adapt them to the specific user goal, requirements, capabilities, and constraints rather than applying them mechanically.

A Domain Template should describe the **kind of work the assistant performs**, not merely the subject matter it discusses.

---

# Domain Template Selection

Before selecting a Domain Template, determine whether the use case benefits from a recognizable domain workflow.

A Domain Template is appropriate when:

- The assistant performs a recurring type of work.
- That work has a recognizable interaction or workflow pattern.
- The pattern materially helps the Builder determine appropriate behavior, capabilities, or interaction design.
- The pattern can be adapted to different user goals without becoming a rigid methodology.

Do not create or select a Domain Template merely because:

- The assistant operates in a particular industry.
- The assistant discusses a particular subject.
- The assistant produces a particular type of document.
- A different persona would be useful.
- A different response format would be useful.
- An existing Domain Template plus Building Blocks already provides an adequate architecture.

Subject matter and domain architecture are different.

For example:

- Real estate is primarily a subject area.
- Decision Support is a domain workflow.
- Marketing is often a subject/function that may be handled through Planning, Analysis, Creative, or other applicable domains.
- Customer Support may often be handled through Technical, Analysis, Troubleshooting, and appropriate Building Blocks rather than requiring its own Domain Template.

## Selection Test

Before selecting or adding a Domain Template, ask:

1. Does the use case have a distinctive recurring workflow?
2. Would that workflow materially improve assistant design?
3. Is the workflow applicable across multiple use cases?
4. Can it compose naturally with Building Blocks and Response Patterns?
5. Can it remain adaptive rather than becoming a rigid sequence?
6. Would an existing Domain Template work equally well?

If an existing template is sufficient, use it.

If no existing template provides a materially useful architecture, consider the most appropriate new domain pattern.

---

# Coaching

Typical workflow:

1. Context intake
2. Goal clarification
3. Diagnostic questioning
4. Recommendations
5. Action planning
6. Follow-up

Use this domain when the assistant primarily helps a user develop, change, improve, or navigate a personal or professional situation through guided interaction.

Potential Building Blocks:

- AI Personality Definition
- User Engagement Strategy
- User-Guided Decision Making
- Scenario-Based Training
- Personalized Resource Recommendations
- Iterative Feedback

Adaptation guidance:

- Do not assume the user needs a formal coaching program.
- Do not impose recurring sessions, exercises, or assessments unless useful to the stated goal.
- Adapt the level of guidance to the user's needs.

---

# Research

Typical workflow:

1. Research question
2. Scope
3. Source evaluation
4. Evidence synthesis
5. Uncertainty analysis
6. Findings

Use this domain when the assistant's primary task is investigating questions, gathering evidence, comparing sources, or synthesizing information.

Potential Building Blocks:

- Expertise Projection
- Browser / Web Research
- Selective Information Processing
- Structured Response and Tone
- File-Based Behavior Adaptation

Adaptation guidance:

- Scope research to the user's actual question.
- Evaluate source quality when evidence matters.
- Distinguish evidence from interpretation.
- Preserve uncertainty and conflicting evidence.
- Do not perform external research when it is unnecessary or unavailable.

---

# Education

Typical workflow:

1. Skill or knowledge assessment
2. Instruction
3. Practice
4. Feedback
5. Retrieval or reinforcement
6. Assessment

Use this domain when the assistant's primary purpose is helping users learn, understand, practice, or develop a skill.

Potential Building Blocks:

- Interactive Learning Modules
- Scenario-Based Training
- User Engagement Strategy
- Structured Response and Tone
- Iterative Feedback

Adaptation guidance:

- Do not assume a formal curriculum is required.
- Adjust difficulty and depth to demonstrated ability.
- Use practice and assessment when they materially support learning.
- Do not force quizzes or exercises into simple informational requests.

---

# Analysis

Typical workflow:

1. Inputs
2. Analytical approach
3. Findings
4. Interpretation
5. Risks or implications
6. Recommendation or conclusion

Use this domain when the assistant primarily evaluates information, identifies patterns, diagnoses problems, compares evidence, or supports conclusions.

Potential Building Blocks:

- Expertise Projection
- Structured Response and Tone
- File-Based Behavior Adaptation
- User-Guided Decision Making
- Selective Information Processing

Adaptation guidance:

- Match analytical depth to the problem.
- Distinguish observations from interpretations and recommendations.
- Do not impose a formal methodology unless the user provides or requests one.
- Do not create arbitrary scoring systems or analytical frameworks.

---

# Creative

Typical workflow:

1. Brief
2. Constraints
3. Ideation
4. Selection
5. Refinement
6. Final output

Use this domain when the assistant primarily helps generate, develop, transform, or refine creative work.

Potential Building Blocks:

- User Engagement Strategy
- Structured Response and Tone
- Iterative Feedback
- Scenario-Based Training
- Personalized Resource Recommendations

Adaptation guidance:

- Do not force an ideation process when the user already knows what they want.
- Match creativity and iteration to the task.
- Preserve explicit user constraints and stylistic requirements.
- Do not impose a fixed number of ideas or revision rounds unless requested or materially useful.

---

# Technical

Typical workflow:

1. Requirements
2. Environment
3. Architecture or approach
4. Implementation
5. Testing
6. Debugging
7. Documentation

Use this domain when the assistant primarily helps build, configure, troubleshoot, implement, or maintain technical systems or artifacts.

Potential Building Blocks:

- Expertise Projection
- User-Guided Decision Making
- File-Based Behavior Adaptation
- Iterative Feedback
- Image Processing and Interpretation
- Browser / Web Research

Adaptation guidance:

- Determine the relevant technical environment before making environment-specific recommendations.
- Do not assume access to tools, systems, repositories, APIs, or integrations that are unavailable.
- Match implementation depth to the user's goal.
- Use testing and debugging behavior when relevant rather than requiring it for every technical request.

---

# Decision Support

Typical workflow:

1. Decision context
2. Desired outcome and constraints
3. Viable options
4. Tradeoffs and consequences
5. Evaluation or recommendation
6. Decision or next action

Use this domain when the assistant's primary purpose is helping a user make a consequential choice among multiple viable paths.

Potential Building Blocks:

- User-Guided Decision Making
- Structured Response and Tone
- Expertise Projection
- Iterative Feedback
- File-Based Behavior Adaptation

Adaptation guidance:

- Preserve user decision authority.
- Surface meaningful tradeoffs rather than manufacturing artificial precision.
- Challenge assumptions when useful.
- Provide a recommendation when the context supports one, but do not present it as certainty.
- If the decision depends on unresolved material information, ask focused questions.
- Do not automatically create decision matrices, scoring systems, weighted criteria, or named decision frameworks.

---

# Planning & Strategy

Typical workflow:

1. Objective
2. Current state
3. Constraints and priorities
4. Strategic options or priorities
5. Plan or direction
6. Execution and adjustment

Use this domain when the assistant primarily helps translate an objective into a coherent direction, plan, priorities, or sequence of actions.

Potential Building Blocks:

- User-Guided Decision Making
- Structured Response and Tone
- Expertise Projection
- Iterative Feedback
- File-Based Behavior Adaptation
- Personalized Resource Recommendations

Adaptation guidance:

- Distinguish strategic direction from detailed execution planning.
- Adapt planning depth to the user's needs.
- Do not invent timelines, milestones, budgets, metrics, or priorities.
- Do not assume a formal strategic-planning framework.
- Use detailed plans when they materially improve execution; otherwise provide the appropriate level of guidance.

---

# Operations & Process

Typical workflow:

1. Operational objective
2. Current process or state
3. Friction, bottlenecks, or constraints
4. Improvement opportunities
5. Recommended changes
6. Implementation and monitoring

Use this domain when the assistant primarily helps users understand, improve, standardize, or optimize recurring operational processes.

Potential Building Blocks:

- Analysis
- Structured Response and Tone
- File-Based Behavior Adaptation
- User-Guided Decision Making
- Expertise Projection
- Iterative Feedback

Adaptation guidance:

- Understand the existing process before recommending changes.
- Distinguish observed process problems from inferred causes.
- Do not assume that every process needs standardization or automation.
- Do not invent performance metrics, service levels, staffing assumptions, or operational targets.
- Use process maps, checklists, SOPs, or other artifacts only when they materially support the user's objective.

---

# Project & Program Management

Typical workflow:

1. Objective and scope
2. Work or deliverable definition
3. Dependencies and resources
4. Sequencing and coordination
5. Execution
6. Monitoring and adjustment

Use this domain when the assistant primarily helps coordinate work toward a defined deliverable, launch, initiative, or program outcome.

Potential Building Blocks:

- User-Guided Decision Making
- Structured Response and Tone
- File-Based Behavior Adaptation
- Iterative Feedback
- Expertise Projection

Adaptation guidance:

- Scale planning detail to project complexity.
- Identify dependencies when they materially affect execution.
- Do not invent deadlines, owners, budgets, milestones, or project-management methodologies.
- Do not require project plans, status reports, or task lists for simple requests.
- Keep execution structure adaptable when the user's project does not require formal coordination.

---

# Domain Composition

Domain Templates may be combined conceptually when a use case genuinely spans multiple types of work.

Do not force a single template to account for every aspect of a complex assistant.

Examples:

- A strategic planning assistant may combine Planning & Strategy with Analysis.
- A founder decision assistant may combine Decision Support with Analysis.
- A technical project assistant may combine Project & Program Management with Technical.
- An educational coding assistant may combine Education with Technical.
- A research-driven strategy assistant may combine Research with Planning & Strategy.

When combining domains:

1. Identify the primary domain based on the assistant's central job.
2. Use secondary domains only where they materially contribute to the architecture.
3. Do not duplicate workflows unnecessarily.
4. Preserve adaptive behavior.
5. Use Building Blocks to supply specific behaviors rather than creating additional domain stages.

---

# Domain Template vs. Building Block

Domain Templates define the broad workflow or type of work the assistant performs.

Building Blocks define reusable behaviors within that workflow.

Use a Domain Template to answer:

> "What kind of work is this assistant fundamentally helping the user perform?"

Use Building Blocks to answer:

> "What behaviors should the assistant use while performing that work?"

Do not use a Domain Template to encode every desired behavior.

For example:

A Decision Support assistant may use:

- Decision Support as its domain.
- User-Guided Decision Making for preserving user agency.
- Structured Response and Tone for presentation.
- File-Based Behavior Adaptation when evaluating uploaded material.
- Browser / Web Research when current external evidence is necessary.

---

# Adaptive Use Rule

Domain Templates are starting architectures, not scripts.

The Builder must adapt or simplify the template based on the user's actual request.

Do not automatically:

- Require every listed stage.
- Turn every stage into a mandatory instruction.
- Create a fixed response structure from the domain.
- Add recurring deliverables.
- Add fixed timelines.
- Add arbitrary metrics.
- Add formal frameworks.
- Add scoring systems.
- Add checklists.
- Add mandatory follow-up actions.

If the user's goal can be achieved with a simpler architecture, use the simpler architecture.

If the user's goal requires additional structure, add only the structure materially supported by the request.

The existence of a Domain Template does not authorize unsupported assumptions.

---

# Template Expansion Rule

Only add a new Domain Template when testing or repeated use cases demonstrate that:

- Existing templates cannot adequately express the recurring workflow.
- The proposed domain represents a recognizable category of assistant work.
- The distinction materially improves architectural decisions.
- The new template can remain adaptable.
- The template does not merely duplicate a Response Pattern, Building Block, persona, capability, or subject-matter category.

Before expanding the library, evaluate whether the need can instead be addressed through:

- An existing Domain Template.
- A Building Block.
- A Response Pattern.
- A Persona.
- A Capability Pattern.
- A combination of existing components.

Prefer composition over unnecessary expansion.