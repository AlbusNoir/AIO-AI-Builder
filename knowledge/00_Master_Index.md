# AI Advantage GPT Builder Knowledge Base
## Master Index

---

# Purpose

This knowledge base supports the design of specialized AI assistants by providing reusable principles, building blocks, domain architectures, response patterns, personas, capability patterns, examples, and quality standards.

The Builder should use the knowledge base as an architectural reference rather than mechanically combining every available component.

---

# Knowledge Modules

## 01 - Design Principles

Defines the foundational principles for designing useful, adaptive, bounded, and reliable assistants.

Use for:

- overall architecture
- design decisions
- adaptive behavior
- assumption handling
- knowledge fidelity
- quality standards

---

## 02 - Instruction Building Blocks

Contains reusable behavioral components for Custom GPT Instructions.

Use when determining:

- interaction behavior
- personality behavior
- file behavior
- research behavior
- image behavior
- learning behavior
- response behavior
- other recurring assistant behaviors

Building Blocks should be selected according to the user's specific goal.

---

## 03 - Domain Templates

Contains starting architectures for recurring kinds of work.

### Current Templates

1. Coaching
2. Research
3. Education
4. Analysis
5. Creative
6. Technical
7. Decision Support
8. Planning & Strategy
9. Operations & Process
10. Project & Program Management

Domain Templates describe **what kind of work the assistant performs**.

They are starting architectures, not rigid workflows.

Adapt them to the user's actual requirements.

---

## 04 - Response Patterns

Contains reusable approaches for organizing assistant outputs.

Use when a recognizable response structure materially improves usability.

Examples include:

- explanatory responses
- analytical findings
- comparisons
- recommendations
- step-by-step guidance
- decision support
- planning
- structured summaries

Response Patterns should not be imposed when the user's needs require adaptive structure.

---

## 05 - Persona Library

Contains reusable functional persona archetypes.

### Current Persona Archetypes

1. Expert Advisor
2. Decision Partner
3. Strategic Advisor
4. Analyst
5. Researcher
6. Coach
7. Tutor
8. Facilitator
9. Operator
10. Creative Collaborator
11. Technical Specialist
12. Supportive Guide

Personas define **who the assistant behaves as while performing its work**.

Personas should be adapted to:

- goal
- domain
- expertise
- audience
- tone
- communication style
- authority
- constraints

Use one primary persona by default.

Add a secondary persona only when it materially improves the assistant.

---

## 06 - Tool & Capability Patterns

Contains reusable patterns for selecting and specifying assistant capabilities.

### Current Capability Patterns

1. Web Search
2. Knowledge Base
3. Document Analysis
4. Image Analysis
5. Data Analysis
6. Calculators / Computational Tools
7. Structured Outputs
8. File-Based Behavior Adaptation
9. Scenario / Simulation
10. Interactive Learning
11. External Integrations
12. Personalized Resource Recommendations

Capabilities define **what the assistant needs to use or perform in order to accomplish its workflow**.

Only select capabilities that materially advance the user's objective.

Capabilities must reflect the actual target environment.

---

## 07 - Quality Assurance

Contains tests and standards for evaluating generated assistants.

Use for:

- instruction quality
- architectural coherence
- knowledge fidelity
- boundary handling
- capability integrity
- assumption handling
- response quality

---

## 08 - Assistant Examples

Contains examples of successful assistant designs and patterns.

Use as references for architecture and behavior.

Do not copy examples mechanically when the user's requirements differ.

---

## 09 - Changelog

Records knowledge-base revisions, major changes, testing outcomes, deprecated patterns, limitations, and future additions.

---

# Architecture Relationships

The Builder should distinguish the major architectural layers:

### Domain

**What kind of work is being performed?**

Examples:

- Analysis
- Research
- Planning & Strategy
- Decision Support
- Project Management

### Persona

**What functional role does the assistant perform while doing that work?**

Examples:

- Analyst
- Researcher
- Decision Partner
- Strategic Advisor
- Technical Specialist

### Response Pattern

**How should the resulting information be organized or communicated?**

### Capability

**What inputs, tools, or system abilities are actually required?**

These layers should complement one another rather than duplicate one another.

---

# Domain Selection

Select the primary Domain Template according to the central job the assistant performs.

Use the simplest sufficient architecture.

A secondary domain may be incorporated when another workflow is materially important.

Do not stack domains merely because several activities occur in the same use case.

---

# Persona Selection

Select the persona according to the functional relationship the user needs with the assistant.

Do not select a persona merely because its subject area matches the domain.

Adapt the persona to the user's:

- desired outcome
- expertise level
- preferred interaction style
- tone
- authority expectations
- constraints

---

# Capability Selection

Select capabilities according to actual workflow requirements.

Before adding a capability, determine:

- whether it is necessary
- what input it requires
- what it enables
- when it should be used
- what limitations apply
- what happens if it is unavailable

Prefer the minimum capability set that reliably supports the intended outcome.

---

# Domain + Persona + Capability Composition

A complete assistant architecture may combine all three.

Example:

> **Domain:** Decision Support  
> **Persona:** Decision Partner  
> **Capability:** Data Analysis

Another:

> **Domain:** Research  
> **Persona:** Researcher  
> **Capability:** Web Search

Another:

> **Domain:** Project & Program Management  
> **Persona:** Operator  
> **Capabilities:** Structured Outputs + External Integration

The combination should emerge from the user's actual requirements.

---

# Domain Template vs Building Block

A Domain Template describes a recurring **type of work**.

A Building Block describes a reusable **behavior**.

Do not create a new Domain Template merely because a new Building Block is required.

---

# Persona vs Building Block

A Persona defines the assistant's functional role, expertise, authority, tone, and behavioral stance.

A Building Block defines a specific behavior that can be added to the assistant.

For example:

> Persona: Coach  
> Building Block: Interactive Learning Modules

---

# Capability vs Building Block

A Capability describes what the assistant can use or perform.

A Building Block describes how the assistant should behave when using that capability.

For example:

> Capability: Web Search  
> Building Block: Browser Tool Integration

or:

> Capability: Document Analysis  
> Building Block: File-Based Behavior Adaptation

---

# Response Pattern vs Persona

Persona defines **who/how the assistant behaves**.

Response Pattern defines **how information is organized**.

Do not use a Response Pattern to compensate for an unclear persona or vice versa.

---

# Knowledge Priority

When designing an assistant:

1. Follow the user's explicit requirements.
2. Apply relevant design principles.
3. Select the appropriate Domain Template.
4. Select and adapt the appropriate Persona.
5. Select appropriate Response Patterns.
6. Select only necessary capabilities.
7. Add relevant Building Blocks.
8. Validate against Quality Assurance guidance.

Do not allow library components to override explicit user requirements.

---

# Adaptive Architecture

All templates, personas, response patterns, and capabilities are starting points.

The Builder should:

- select what is relevant
- adapt what is useful
- omit what is unnecessary
- combine components when justified
- avoid arbitrary complexity

The goal is not to maximize the number of components.

The goal is to produce the **simplest architecture that reliably achieves the user's intended outcome**.

---

# Version

**Knowledge Base:** 1.3  
**Updated:** 2026-09-11

**Primary change:** Expanded the Persona and Tool & Capability libraries with reusable archetypes, capability patterns, selection guidance, composition rules, and capability-integrity guidance.