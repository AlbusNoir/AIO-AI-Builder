# Quality Assurance

Evaluate every generated assistant against the following criteria.

QA should evaluate both **configuration quality** and **behavioral fidelity**.

---

# Goal Alignment

Does the assistant optimize for the user's stated outcome?

Does every major workflow, behavior, capability, knowledge requirement, and response structure materially support that outcome?

Remove features that do not contribute meaningfully.

---

# Behavioral Specificity

Are instructions operational rather than vague?

Can the desired behavior be recognized and evaluated?

Is specificity useful, or has the Builder added unnecessary detail merely to make the assistant appear sophisticated?

---

# Interaction Quality

Does the assistant ask useful questions without creating unnecessary friction?

Does it know when to proceed versus clarify?

When information is missing, does it ask only when the missing information materially affects behavior?

---

# Knowledge Grounding

Does the assistant use authoritative information appropriately?

Does it distinguish:

- provided knowledge
- recommended knowledge
- general reference information
- inference

Does it avoid unsupported claims?

---

# Source Fidelity

When the user provides methodology or authoritative source material, does the assistant preserve:

- terminology
- meaning
- semantic boundaries
- organization
- level of detail
- uncertainty
- source relationships

Does it avoid silently improving or expanding the source?

---

# Attribution Fidelity

When information comes from different people or sources, does the assistant preserve:

- who made the statement
- whether it was observed, reported, believed, estimated, alleged, or interpreted
- the original level of certainty

Does it avoid converting beliefs or interpretations into facts?

---

# Methodology Fidelity

If the user provides a defined methodology:

- Are its stages preserved?
- Were new stages introduced?
- Were definitions added?
- Were completion criteria invented?
- Were decision rules added?
- Were causal relationships added?
- Was a familiar external framework substituted?

If any substantive methodology was added without support, revise.

---

# Conceptual Framework Discipline

Does the assistant introduce any:

- taxonomy
- diagnostic model
- category system
- causal model
- scoring system
- prioritization framework
- maturity model
- decision model
- funnel
- stages
- dimensions
- root-cause structure

that the user did not provide or request?

If yes, determine whether the addition is genuinely necessary.

If not necessary, remove it.

If necessary but unspecified, either ask the user or clearly label it as a Proposed Design Choice.

---

# Auto Assumption Discipline

If Auto was used:

- Were assumptions necessary?
- Were they strongly implied?
- Were conservative defaults used?
- Were assumptions labeled when material?
- Did the Builder invent numeric parameters?
- Did it invent business conditions?
- Did it invent audience characteristics?
- Did it invent performance targets?
- Did it invent methodologies?
- Did it invent conceptual frameworks?

A useful Auto configuration should be **operational without being presumptuous**.

---

# Specificity Quality

For each notable specific detail, ask:

> "Is this detail explicitly supported, strongly implied, necessary for operation, or a conservative default?"

If none apply, remove it.

Do not justify a detail merely because it is:

- common
- useful
- sophisticated
- familiar
- industry-standard
- likely to work

Common practice is not equivalent to user authorization.

---

# Capability Accuracy

Are capabilities actually available and materially useful?

Does the assistant accurately represent capability limitations?

Does it avoid claiming that it:

- researched something it did not research
- verified something it did not verify
- accessed information it did not access
- performed an action it did not perform

---

# Consistency

Would repeated users receive predictably useful behavior?

Are important instructions sufficiently precise to produce stable behavior?

Does the assistant preserve the same source-fidelity rules across different input formats?

---

# Adaptability

Can the assistant handle reasonable variations of the use case?

Can it adapt when:

- the user provides more information
- the user provides less information
- sources conflict
- the user corrects it
- the task changes within scope
- the user explicitly requests an outside framework

Does it preserve higher-priority constraints during adaptation?

---

# Failure Handling

Does the assistant recognize:

- uncertainty
- missing information
- conflicting information
- unavailable capabilities
- unsupported conclusions
- out-of-scope requests

Does it handle those conditions explicitly rather than guessing?

---

# Output Quality

Are responses:

- appropriately structured
- relevant
- actionable
- aligned with the user's requested format
- appropriately detailed
- free of unnecessary framework or terminology invention

---

# Auto Behavioral Test

When Auto is used, test the generated configuration against a deliberately underspecified request.

Check whether the assistant:

- remains useful
- avoids arbitrary numeric assumptions
- avoids invented frameworks
- avoids invented taxonomies
- avoids invented success criteria
- asks for material missing information at runtime
- distinguishes assumptions from requirements

---

# Out-of-Scope Test

Give the generated assistant a request unrelated to its defined purpose.

Check whether it:

- recognizes the scope boundary
- avoids pretending the request is within scope
- remains concise and useful
- does not invent a new role to satisfy the request

---

# Missing Information Test

Give the assistant insufficient information for a material conclusion.

Check whether it:

- identifies the gap
- avoids filling the gap with plausible assumptions
- asks for relevant information
- preserves what is known

---

# Conflicting Information Test

Provide competing statements from different sources.

Check whether the assistant:

- preserves attribution
- identifies the conflict
- avoids silently choosing a winner
- avoids converting one perspective into objective fact

---

# User Correction Test

Correct an interpretation after the assistant has responded.

Check whether it:

- incorporates the correction
- preserves the intended distinction
- does not defend an unsupported interpretation
- does not invent a new methodology
- maintains source fidelity

---

# Knowledge-Dependent Test

Provide authoritative source material and ask the assistant to use it.

Check whether it:

- uses the provided material
- preserves its terminology
- preserves attribution and uncertainty
- avoids importing unsupported external methodology

---

# Capability-Dependent Test

Ask the assistant to perform an action that requires a capability it does not have.

Check whether it:

- recognizes the limitation
- does not pretend the action was performed
- explains what information or capability would be required
- remains useful within its actual capabilities

---

# Simple Task Test

Give the assistant a straightforward request within scope.

Check whether it responds efficiently rather than activating unnecessary workflows, frameworks, questions, or features.

---

# Complex Task Test

Give the assistant a complex request involving multiple constraints.

Check whether it:

- preserves the user's priorities
- maintains source fidelity
- handles uncertainty
- uses appropriate capabilities
- produces a coherent output
- avoids unnecessary complexity

---

# Severity Levels

Classify QA findings as:

### Critical
- fabricated facts, sources, actions, capabilities, or evidence
- violation of an explicit user boundary
- substantive methodology invention when the user explicitly prohibited it
- material attribution failure
- materially misleading capability claims

### High
- major goal misalignment
- unsupported causal conclusions
- substantial semantic drift
- significant Auto-generated framework invention
- incorrect source priority

### Medium
- unnecessary specificity
- minor workflow rigidity
- unnecessary capability
- avoidable verbosity
- minor source classification issue

### Low
- stylistic inconsistency
- minor formatting issue
- non-material wording improvement

---

# Scoring

Score each applicable criterion from 1-5:

**1 - Poor**  
Behavior is unreliable or materially misaligned.

**2 - Weak**  
Major improvement required.

**3 - Adequate**  
Generally functional but has meaningful weaknesses.

**4 - Strong**  
Reliable with minor imperfections.

**5 - Excellent**  
Clear, reliable, appropriately constrained, and deployable.

A Critical issue requires revision regardless of aggregate score.

---

# Revision Loop

When QA identifies a problem:

1. Identify the specific failure.
2. Determine whether it originated in requirements, architecture, knowledge selection, capability design, or instructions.
3. Correct the smallest necessary layer.
4. Re-run the relevant behavioral test.
5. Re-check previously successful behaviors for regression.

Do not rewrite the entire architecture to fix a localized problem.

---

# Final Pre-Deployment Check

Verify:

- The assistant has a specific job.
- Its behavior directly supports the desired outcome.
- Instructions are operational and testable.
- The interaction workflow is clear.
- Knowledge requirements are appropriate.
- Tool requirements are appropriate.
- Constraints are respected.
- Failure and uncertainty are handled.
- Attribution is preserved.
- User methodology is preserved.
- No unsupported conceptual framework has been introduced.
- Auto assumptions are conservative and transparent.
- The configuration is practical to deploy.

---

# Final QA Question

Before approving the assistant, ask:

> "Did the Builder make this assistant more useful, or merely more elaborate?"

If an element makes the assistant more elaborate without materially improving its behavior, remove it.