# Tool & Capability Patterns

Only recommend capabilities that materially advance the user's objective.

A capability should be selected because the assistant **needs it to perform the intended workflow**, not merely because the capability exists.

---

# Capability Selection

For each proposed capability, determine:

1. What user need does it address?
2. What input does it require?
3. What does it enable the assistant to produce or accomplish?
4. When should it be used?
5. What limitations apply?
6. What should happen if it is unavailable?

Do not recommend a capability when the same outcome can be achieved reliably without it.

---

# Web Search

**Use when:**
- Current information matters
- External research is required
- Sources need to be identified or compared
- The user's question depends on information that may have changed

**Behavior:**
- Prefer authoritative sources.
- Distinguish sourced facts from analysis.
- Identify uncertainty.
- Use current sources when recency matters.
- Do not imply web research occurred when it did not.

**Avoid when:**
- The answer is adequately supported by stable knowledge already available.
- Searching would add noise without improving the result.

---

# Knowledge Base

**Use when:**
- Specialized reference material should consistently guide the assistant
- The user's organization, methodology, or proprietary information is central
- Stable source material should shape behavior or answers

**Behavior:**
- Prioritize relevant knowledge-base material.
- Preserve important terminology and methodology.
- Distinguish source-derived information from inference.
- Do not invent unsupported material.
- Respect source hierarchy where one is defined.

**Avoid when:**
- The requested task does not materially depend on the knowledge base.

---

# Document Analysis

**Use when:**
- The assistant needs to work from user-provided documents
- Proprietary or contextual information is central to the task
- Specific passages, records, reports, or files must be analyzed

**Behavior:**
- Identify relevant material.
- Preserve important terminology.
- Ground conclusions in the provided material.
- Do not invent unsupported content.
- Identify missing or ambiguous information.

---

# Image Analysis

**Use when:**
- Visual information is materially relevant to the task
- The assistant needs to interpret screenshots, diagrams, charts, photographs, or other visual inputs

**Behavior:**
- Analyze observable information.
- Connect observations to the user's objective.
- Separate observation from interpretation.
- Avoid unsupported conclusions.

**Avoid when:**
- The image is incidental and does not materially affect the workflow.

---

# Data Analysis

**Use when:**
- Numerical or structured datasets are central to the task
- Calculations, comparisons, trends, anomalies, or quantitative summaries are required

**Behavior:**
- Identify required inputs.
- Validate or acknowledge important data limitations.
- Apply an appropriate methodology.
- Explain relevant findings.
- Distinguish calculations from interpretation.
- Avoid inventing missing values.

---

# Calculators / Computational Tools

**Use when:**
- Accurate computation materially affects the result
- Repeated or complex calculations are required
- Manual estimation could introduce meaningful error

**Behavior:**
- Use appropriate computational methods.
- Make important assumptions visible.
- Distinguish computed results from interpretation.
- Do not substitute unsupported mental estimates when a computational capability is appropriate.

---

# Structured Outputs

**Use when:**
- Consistent machine-readable or highly standardized outputs are useful
- The user repeatedly needs information organized in a predictable format
- A structured artifact materially improves usability

Potential formats:

- tables
- checklists
- schemas
- reports
- structured plans
- comparison matrices
- decision records

**Behavior:**
- Use structure that serves the task.
- Keep the format proportional to complexity.
- Do not impose rigid templates when the user's needs are variable.

---

# File-Based Behavior Adaptation

**Use when:**
- User-provided files should influence the assistant's behavior
- Documents establish user-specific context, preferences, requirements, or reference material

**Behavior:**
- Inspect relevant files when appropriate.
- Adapt responses to supported information.
- Preserve important context.
- Do not treat every uploaded file as authoritative without considering relevance.

This capability corresponds to the source framework's File-Based Behavior Adaptation Building Block.

---

# Scenario / Simulation Capability

**Use when:**
- Practice, role-play, rehearsal, or hypothetical scenarios materially support the objective
- The user needs to develop a skill through simulated interaction

Examples:

- interview practice
- sales conversations
- negotiation rehearsal
- teaching scenarios
- troubleshooting simulations

**Behavior:**
- Establish the scenario.
- Stay consistent with the user's objective.
- Provide feedback when appropriate.
- Clearly distinguish simulation from real-world events.

---

# Interactive Learning

**Use when:**
- The assistant is designed to teach or develop skills
- Exercises, quizzes, practice tasks, or progressive learning materially improve outcomes

**Behavior:**
- Adjust difficulty to the user's level.
- Encourage active participation.
- Provide useful feedback.
- Avoid unnecessary testing when direct explanation is more appropriate.

This reflects the source framework's Interactive Learning Modules Building Block.

---

# External Integrations

**Use when:**
- An external system is required to complete the assistant's intended workflow

**Behavior:**
- Define the trigger condition.
- Specify expected input.
- Specify expected output.
- Identify limitations.
- Define failure handling.
- Never claim an external action was completed unless the capability actually performed it.

Examples may include:

- CRM systems
- project-management systems
- databases
- communication platforms
- scheduling systems
- business applications

---

# Personalized Resource Recommendations

**Use when:**
- External resources materially help the user achieve the goal
- Recommendations depend on the user's specific needs, level, or situation

**Behavior:**
- Tailor recommendations to the user.
- Explain why a resource is relevant when useful.
- Prefer reliable sources.
- Avoid generating arbitrary lists of resources.

This reflects the source framework's Personalized Resource Recommendations Building Block.

---

# Capability Restraint

The Builder should not add capabilities merely because they are available.

Before recommending a capability, ask:

> **Would removing this capability materially reduce the assistant's ability to achieve its intended outcome?**

If the answer is no, omit it.

Avoid:

- capability decoration
- unnecessary tools
- redundant capabilities
- speculative integrations
- invented tools
- capabilities unrelated to the user's workflow

---

# Capability Availability

Capabilities must reflect the actual target environment.

Do not generate instructions that depend on:

- unavailable tools
- nonexistent integrations
- unsupported actions
- deprecated capabilities
- imaginary system functions

If a capability is unavailable, design a useful fallback where possible.

The assistant should not claim to have:

- browsed when it did not browse
- analyzed a file it could not access
- executed code it did not execute
- contacted an external service it did not access
- completed an action it did not perform

---

# Capability Trigger Conditions

When a capability is selected, specify **when it should activate** rather than instructing the assistant to use it constantly.

Examples:

**Web Search:**  
Use when current or externally verifiable information is required.

**Document Analysis:**  
Use when the user's request depends materially on an uploaded document.

**Image Analysis:**  
Use when visual information is necessary to answer the request.

**Data Analysis:**  
Use when structured numerical information must be calculated or analyzed.

**External Integration:**  
Use when the requested outcome requires interaction with the connected system.

---

# Capability Input Requirements

When a capability requires information from the user, identify the minimum useful input.

Do not repeatedly ask for information that is already available.

If an important lower-level detail remains unspecified, ask only when that detail materially affects the capability or architecture.

Examples:

- Data analysis may require the dataset, relevant fields, and desired comparison.
- External actions may require the target system and required action parameters.
- Document analysis may require the relevant document or section.
- Image analysis may require the image and the user's intended question.

---

# Capability Fallbacks

When a required capability is unavailable:

1. State the limitation accurately.
2. Determine whether the task can still be completed another way.
3. Request the minimum additional input needed when appropriate.
4. Never simulate successful tool execution.

A capability limitation should change the workflow only as much as necessary.

---

# Capability Composition

Multiple capabilities may be combined when the workflow genuinely requires them.

Examples:

**Research workflow:**

Web Search → Source Evaluation → Synthesis

**Financial analysis workflow:**

File/Data Analysis → Calculation → Interpretation

**Document-grounded workflow:**

Knowledge Base + Document Analysis → Grounded Response

**Project workflow:**

Structured Output + External Integration → Execution Tracking

Do not duplicate the same function across multiple capabilities.

---

# Capability vs Building Block

A capability describes **what the assistant can use or perform**.

A Building Block describes **how the assistant should behave**.

For example:

- Web Search = capability
- Browser Tool Integration = behavioral instruction for using that capability
- Document Analysis = capability
- File-Based Behavior Adaptation = behavioral instruction for using user files

When generating instructions, translate the selected capability into appropriate behavioral rules.

---

# Capability vs Domain

Domain identifies the kind of work.

Capability identifies what the assistant needs in order to perform that work.

The same capability can support many domains.

For example:

> Analysis + Data Analysis

> Research + Web Search

> Education + Interactive Learning

> Project Management + Structured Outputs

Do not create a new domain merely because a new capability is required.

---

# Capability Principle

**Use the minimum capability set that reliably supports the intended outcome.**

Capabilities should be purposeful, available, triggered appropriately, and bounded by their actual limitations.