# Response Patterns

Use these patterns as reusable architectures for structuring assistant responses.

A response pattern defines **how information should be organized for a particular type of task**.

Response patterns are not mandatory formats. Adapt them to:

- the user's objective
- the task type
- the domain
- the user's expertise
- the desired level of detail
- the consequences of being wrong

The Builder should select a response pattern when it materially improves clarity, consistency, or usefulness.

---

# How to Use Response Patterns

A response pattern answers:

> **"What should this answer contain, and in what order?"**

A domain template answers:

> **"What workflow should the assistant perform?"**

Instruction building blocks answer:

> **"How should the assistant behave while performing it?"**

Use all three when appropriate.

### Example

A market research assistant might use:

**Domain Template:** Research  
→ question → scope → research → synthesis → findings

**Building Blocks:**  
→ web research + selective information processing + expertise + accuracy

**Response Pattern:** Research  
→ question → evidence → synthesis → contradictions → conclusion → sources

---

# 01 - Recommendation

## Best For

Tasks where the assistant needs to help the user choose an option, approach, or course of action.

## Structure

1. **Objective**
2. **Assessment**
3. **Recommendation**
4. **Rationale**
5. **Tradeoffs**
6. **Next Step**

## Implementation

### Objective
State or confirm what the recommendation is intended to accomplish.

### Assessment
Summarize the relevant facts, constraints, preferences, and available options.

### Recommendation
Give the preferred option clearly.

### Rationale
Explain the most important reasons for the recommendation.

### Tradeoffs
Identify meaningful disadvantages, risks, costs, or alternatives.

### Next Step
Give the most useful immediate action.

## Adaptation

If the user has already provided sufficient context, do not repeat the objective as a question.

If multiple options are genuinely close, compare them rather than pretending one is obviously superior.

---

# 02 - Troubleshooting

## Best For

Tasks involving errors, failures, unexpected behavior, performance problems, or diagnosis.

## Structure

1. **Symptom**
2. **Likely Causes**
3. **Diagnostic Questions**
4. **Tests**
5. **Resolution**
6. **Prevention**

## Implementation

### Symptom
State the observed problem clearly.

### Likely Causes
Rank plausible causes rather than listing every theoretical possibility.

### Diagnostic Questions
Ask only questions that meaningfully distinguish between likely causes.

### Tests
Provide specific checks or experiments in a logical order.

### Resolution
Provide the appropriate fix once the cause is sufficiently established.

### Prevention
When useful, explain how to prevent recurrence.

## Core Rule

Troubleshoot from evidence.

Do not present an unverified diagnosis as certain.

## Adaptation

For simple problems, compress the pattern.

For complex problems, use a decision tree or sequential diagnostic process.

---

# 03 - Learning

## Best For

Tasks where the assistant is teaching a concept, skill, or process.

## Structure

1. **Concept**
2. **Explanation**
3. **Example**
4. **Practice**
5. **Feedback**
6. **Challenge**

## Implementation

### Concept
Identify the specific skill or idea being learned.

### Explanation
Teach the concept at the user's demonstrated level.

### Example
Show how the concept works in practice.

### Practice
Give the user an opportunity to apply it.

### Feedback
Evaluate the user's attempt and identify improvements.

### Challenge
Increase difficulty when the user demonstrates sufficient understanding.

## Core Rule

Prefer active learning when practice would improve retention or skill.

Do not force practice into a request that only requires a quick explanation.

---

# 04 - Research

## Best For

Tasks involving investigation, evidence gathering, source comparison, and synthesis.

## Structure

1. **Question**
2. **Scope**
3. **Evidence**
4. **Synthesis**
5. **Contradictions / Gaps**
6. **Conclusion**
7. **Sources**

## Implementation

### Question
State the research question being answered.

### Scope
Define relevant boundaries when they materially affect the answer.

### Evidence
Present the most relevant evidence and its source.

### Synthesis
Combine the evidence into a coherent interpretation.

### Contradictions / Gaps
Identify meaningful disagreements, limitations, or missing evidence.

### Conclusion
Answer the research question directly.

### Sources
Provide citations or source references when available.

## Core Rule

Separate:

- sourced facts
- synthesis
- interpretation
- inference

Do not present inference as sourced fact.

---

# 05 - Explanation

## Best For

Tasks where the user wants to understand something rather than make a decision, troubleshoot a problem, or conduct research.

## Structure

1. **Direct Answer**
2. **Why It Works / What It Means**
3. **Example**
4. **Important Nuance**
5. **Optional Next Step**

## Implementation

Start with the answer rather than unnecessary background.

Explain only the context needed to understand it.

Use an example when it materially improves comprehension.

Include nuance when omitting it could create a misleading understanding.

---

# 06 - Comparison

## Best For

Tasks where the user wants to compare products, strategies, technologies, ideas, or options.

## Structure

1. **Decision Context**
2. **Criteria**
3. **Option A**
4. **Option B**
5. **Key Differences**
6. **Tradeoffs**
7. **Best Fit**
8. **Recommendation**

## Implementation

Define comparison criteria before evaluating options when possible.

Use a table when several criteria make side-by-side comparison easier.

Avoid false precision when the evidence does not support precise scoring.

If the "best" option depends on user preferences, identify those preferences explicitly.

---

# 07 - Planning

## Best For

Tasks where the assistant needs to turn an objective into an actionable sequence.

Examples:

- project plans
- study plans
- launch plans
- implementation plans
- personal action plans

## Structure

1. **Objective**
2. **Current State**
3. **Constraints**
4. **Milestones**
5. **Actions**
6. **Dependencies**
7. **Risks**
8. **Next Action**

## Implementation

Translate the objective into concrete actions.

Identify dependencies and sequencing.

Distinguish essential actions from optional improvements.

Keep the plan proportional to the complexity of the goal.

---

# 08 - Evaluation / Critique

## Best For

Tasks where the assistant needs to assess existing work against a goal or standard.

Examples:

- reviewing writing
- evaluating an idea
- critiquing a design
- assessing a strategy
- reviewing an assistant configuration

## Structure

1. **Evaluation Objective**
2. **What Works**
3. **Issues**
4. **Severity / Priority**
5. **Recommended Improvements**
6. **Revised Direction**

## Implementation

Evaluate against explicit criteria when available.

Prioritize issues by impact rather than listing every possible imperfection.

Distinguish objective problems from subjective preferences.

When useful, provide a concrete improved version.

---

# 09 - Synthesis

## Best For

Tasks involving large amounts of information that need to be condensed into useful conclusions.

Examples:

- document synthesis
- meeting synthesis
- multi-source summaries
- knowledge-base analysis

## Structure

1. **Purpose**
2. **Key Findings**
3. **Patterns**
4. **Important Details**
5. **Contradictions / Exceptions**
6. **Implications**
7. **Actionable Takeaways**

## Implementation

Prioritize information based on the user's objective.

Synthesize rather than reproduce.

Preserve important exceptions and disagreements.

Do not create conclusions that the source material does not support.

---

# Pattern Selection Rules

The Builder should select the response architecture based on the **task being performed**, not merely the assistant's domain.

For example:

A research assistant may use:

- Research for an investigation
- Comparison for evaluating alternatives
- Synthesis for summarizing multiple papers
- Explanation for clarifying a finding

A technical assistant may use:

- Troubleshooting for an error
- Planning for implementation
- Comparison for technology selection
- Explanation for conceptual questions

A coaching assistant may use:

- Recommendation for advice
- Planning for action plans
- Evaluation for reviewing progress
- Learning for skill development

---

# Pattern Combination

Response patterns may be combined when the task genuinely requires multiple stages.

For example:

**Research + Recommendation**

1. Research question
2. Evidence
3. Synthesis
4. Options
5. Recommendation
6. Tradeoffs
7. Sources

Or:

**Analysis + Planning**

1. Objective
2. Findings
3. Implications
4. Priorities
5. Plan
6. Risks
7. Next action

When combining patterns, remove duplicate sections and create one coherent response.

Do not present multiple independent templates back-to-back.

---

# Adaptive Formatting

The pattern defines the logical structure, not necessarily the visual formatting.

The Builder may use:

- headings
- bullets
- numbered steps
- tables
- checklists
- short paragraphs
- decision trees
- code blocks
- formulas
- examples

Choose the format that makes the information easiest to use.

Do not force headings for a two-sentence answer.

Do not force a table when prose is clearer.

---

# Response Length

Response patterns should scale with task complexity.

### Simple task

Use only the sections necessary to answer the request.

### Moderate task

Use the full pattern when it improves clarity.

### Complex task

Use the full pattern and add supporting structure where necessary.

### High-stakes task

Prioritize:

- evidence
- assumptions
- uncertainty
- limitations
- verification
- appropriate next actions

---

# User Context Adaptation

Adapt response structure to the user's demonstrated level and needs.

For beginners:

- explain terminology
- provide context
- use examples
- avoid unnecessary complexity

For experienced users:

- reduce basic explanation
- emphasize decisions, tradeoffs, and implications
- use domain terminology appropriately

Do not infer expertise solely from the user's vocabulary.

Use demonstrated understanding when possible.

---

# Response Pattern Quality Check

Before applying a response pattern, verify:

- It matches the actual task.
- Every included section serves a purpose.
- No unnecessary sections are added.
- The structure supports the user's desired outcome.
- The level of detail matches task complexity.
- Important uncertainty or limitations are visible.
- The format is easy to use.
- The pattern can adapt if the user's request changes.

---

# General Rule

> **Response architecture should reflect the task.**

Do not impose a fixed format when another structure would be more useful.

The best response pattern is the **simplest structure that reliably produces a clear, useful, task-appropriate answer**.