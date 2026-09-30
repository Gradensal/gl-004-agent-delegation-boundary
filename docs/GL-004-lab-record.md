# GRADENSAL LAB RECORD

## Lab ID

GL-004

## Project

Agent Delegation Boundary Lab

## Date Started

September 30, 2026

## Date Completed

September 30, 2026

## Project Status

Research Prototype

Not production-ready.

---

## Research Question

When a persistent AI agent proposes an action, which actions should it perform
autonomously, which should require human approval, and which should remain
outside delegated authority?

A related question emerged during the experiment:

> How much human approval should an always-on agent require before the approval
> mechanism itself becomes operationally burdensome?

---

## Problem

Persistent AI agents can continue working toward goals while humans are not
actively supervising every action.

That creates a delegation problem.

Grant too little autonomy and the agent may interrupt a human for routine,
low-risk work.

Grant too much autonomy and the agent may perform consequential actions without
appropriate human oversight.

The architectural problem is therefore not simply whether a human remains
"in the loop."

The more precise question is:

> Where should the human decision boundary sit?

GL-004 explores that problem by separating an agent's intention to perform an
action from its authority to execute that action.

---

## Core Concept

Every proposed agent action is evaluated through a deterministic delegation
policy before execution.

The policy returns one of three decisions:

- **ACT** — the agent may proceed autonomously
- **ASK** — human approval is required
- **BLOCK** — the action falls outside delegated authority

This creates an explicit control boundary between agent reasoning and agent
execution.

---

## Architecture

```text
Persistent Agent
      |
      v
Action Proposal
      |
      v
Delegation Policy Engine
      |
      +--------+--------+
      |        |        |
     ACT      ASK     BLOCK
      |        |        |
      v        v        v
 Execute    Human     Reject
           Approval
      \        |        /
       \       |       /
        +------v------+
        Audit Ledger
```

---

## Architecture Principle

The central architectural principle is:

> Agent reasoning proposes. Deterministic policy disposes.

An AI agent may reason probabilistically about what it wants to do.

The final delegation decision remains separate, deterministic, inspectable,
and testable.

The agent does not automatically receive execution authority simply because it
generated a valid action proposal.

---

## Technologies

- Python 3.12.6
- Pydantic 2.13.5
- pytest 8.4.2
- JSON
- JSONL
- Git
- GitHub
- GitHub Actions

---

## Main Components

### `models.py`

Defines structured data models for:

- action proposals
- policy decisions
- decision types

An action proposal records information including:

- agent ID
- action
- affected resource
- external effects
- financial effects
- credential effects
- state changes
- data sensitivity
- contextual metadata

---

### `policy.py`

Contains the deterministic delegation policy engine.

The engine evaluates action proposals and resolves them to:

- ACT
- ASK
- BLOCK

The engine also implements policy precedence so that higher-consequence
conditions are evaluated before lower-risk autonomous permissions.

Unknown actions fail closed to:

**ASK**

rather than automatically receiving authority.

---

### `policies.json`

Contains the configurable prototype policy.

It defines:

- autonomous actions
- approval-required actions
- explicitly blocked actions
- policy version
- sensitive-data threshold

Externalizing selected policy configuration makes the delegation rules easier
to inspect and modify.

---

### `ledger.py`

Creates an append-only JSONL decision ledger.

Each record contains:

- the original action proposal
- the resulting policy decision
- policy identifier
- policy version
- evaluation timestamp
- experiment scenario

This makes policy decisions auditable after execution.

---

### `simulation.py`

Builds the deterministic synthetic workday and evaluates it under two different
delegation strategies.

It also calculates experiment metrics including:

- total actions
- ACT count
- ASK count
- BLOCK count
- approval rate
- autonomous rate
- blocked rate

---

### `run_demo.py`

Runs the complete experiment.

It:

1. loads the delegation policy;
2. creates the synthetic workday;
3. evaluates the same workload under both policies;
4. records audit traces;
5. calculates the comparison;
6. writes machine-readable evidence;
7. writes human-readable evidence;
8. prints the results to the terminal.

---

## Policy Precedence

Policy evaluation order matters.

The prototype conceptually evaluates conditions in this order:

```text
Explicitly blocked action
        |
        v
Credential effect
        |
        v
Financial effect
        |
        v
Configured approval action
        |
        v
External effect
        |
        v
State change
        |
        v
Sensitive data
        |
        v
Configured autonomous action
        |
        v
Unknown action
        |
        v
ASK
```

This means a lower-risk permission cannot override a higher-consequence
condition.

---

## Experiment

A deterministic synthetic workday containing:

**100 proposed agent actions**

was evaluated under two policies.

### Policy A — Ask Everything

Every action that is not explicitly blocked requires human approval.

### Policy B — Risk-Based Delegation

The deterministic policy engine evaluates each proposal and resolves it to:

- ACT
- ASK
- BLOCK

using configured action classes and contextual properties.

Both policies receive the exact same 100 action proposals.

---

## Synthetic Workload

The workload contains:

- 75 low-risk internal actions
- 20 consequential actions
- 1 previously unknown action
- 4 explicitly prohibited actions

Examples include:

- reading internal documents
- searching internal knowledge
- summarizing internal reports
- drafting internal notes
- sending external email
- publishing content
- updating an external system
- issuing refunds
- transferring money
- changing passwords
- encountering an unknown connector action

---

## Results

### Ask-Everything Policy

- ACT: 0
- ASK: 96
- BLOCK: 4
- Approval burden: 96%

### Risk-Based Delegation

- ACT: 75
- ASK: 21
- BLOCK: 4
- Approval burden: 21%

---

## Observed Difference

In this synthetic workload, risk-based delegation produced:

- **75 fewer human approval requests**
- approval burden reduced from **96% to 21%**
- a **75 percentage-point difference**
- the same **4 explicitly prohibited actions remained blocked**

Across both policy scenarios, the experiment produced:

**200 auditable policy decisions**

---

## Important Interpretation

The experiment demonstrates that the placement of a delegation boundary can
materially change human interruption volume while the underlying workload
remains identical.

It does not establish that fewer approvals are inherently safer, better, more
efficient, or more appropriate for real organizations.

The project measures:

**approval volume**

It does not measure:

- actual human approval fatigue
- human attention quality
- approval accuracy
- safety outcomes
- productivity
- organizational trust
- regulatory compliance
- real-world operational risk

---

## Evidence

Public experiment evidence is stored in:

- `evidence/approval-burden-results.json`
- `evidence/approval-burden-results.md`

The raw runtime audit trace is written to:

- `traces/delegation-decisions.jsonl`

Runtime traces are intentionally excluded from Git through `.gitignore`.

This prevents potentially sensitive operational traces from being committed by
default.

---

## Testing

GL-004 contains:

**14 automated tests**

The test suite covers:

- autonomous internal actions
- approval-required communications
- external side effects
- financial effects
- sensitive data
- credential-changing actions
- explicitly blocked actions
- unknown actions
- fail-closed behavior
- policy precedence
- deterministic 100-action workload
- Ask-Everything baseline
- Risk-Based Delegation results
- JSONL audit logging

---

## Continuous Integration

GitHub Actions independently runs the Python 3.12 test suite on repository
changes.

The CI workflow verifies:

- repository checkout
- Python environment setup
- dependency installation
- source compilation
- automated tests

A passing GitHub Actions run provides independent evidence that the test suite
works outside the local development terminal.

---

## Security Decisions

The prototype deliberately:

- uses synthetic actions only
- does not connect to live external systems
- contains no real production credentials
- performs no real financial transactions
- executes no real external communications
- excludes runtime traces from Git
- separates reasoning from authorization
- fails unknown actions closed to human review
- keeps the core governance logic independent from an LLM

---

## Key Technical Decisions

### 1. Separate intention from execution

An action proposal is created before execution.

This gives the system a point where policy can intervene.

### 2. Keep final delegation deterministic

The policy engine does not ask an LLM whether an action should be permitted.

For the same action proposal and policy configuration, the expected decision is
deterministic.

### 3. Fail unknown actions closed

Unknown actions resolve to:

**ASK**

rather than:

**ACT**

This prevents newly introduced behavior from silently inheriting authority.

### 4. Record decisions

The append-only JSONL ledger preserves both the original proposal and the policy
decision.

This supports auditability and debugging.

### 5. Compare policies using the same workload

The same 100 synthetic actions are evaluated under both policies.

This allows approval volume to be compared without changing the workload.

---

## Skills Practiced

This project strengthened practical understanding of:

- AI agent governance
- persistent-agent architecture
- delegation boundaries
- policy engines
- deterministic authorization
- action modeling
- Pydantic
- structured data validation
- JSON policy configuration
- JSONL audit logging
- policy precedence
- fail-closed design
- experimental design
- synthetic workloads
- unit testing
- edge-case testing
- Git
- GitHub
- GitHub Actions
- CI
- technical documentation
- architecture communication
- responsible technical claims
- experiment evidence
- portfolio engineering

---

## Major Challenges

The primary conceptual challenge was distinguishing:

**human-in-the-loop**

from:

**meaningful human oversight**

Simply requiring approval for every action preserves formal human control but
can create a very high number of interruptions.

This made the location and frequency of the approval boundary an explicit
architectural consideration.

---

## Important Bugs and Lessons

### Lesson 1 — Unknown actions require an explicit default

If the policy engine automatically allowed actions that were not listed in the
policy, newly introduced behavior could unintentionally inherit authority.

The prototype therefore defaults unknown actions to:

**ASK**

### Lesson 2 — Policy precedence matters

An action can have several properties simultaneously.

For example, an explicitly prohibited action may also:

- affect money
- modify state
- create an external effect

The system must evaluate the highest-consequence rule first.

### Lesson 3 — Approval burden is measurable, approval fatigue is not

The experiment can truthfully measure the number of approval requests.

It cannot claim that users became fatigued because no human participants were
tested.

This distinction became an important technical-storytelling lesson.

### Lesson 4 — Runtime evidence and public evidence should be separated

Raw operational traces may contain information that should not automatically
enter source control.

The prototype therefore keeps raw JSONL traces local while committing
summarized experiment evidence.

---

## Key Insight

Human-in-the-loop is not a binary architectural choice.

The more useful questions are:

- Which decisions require a human?
- Which decisions may proceed autonomously?
- Which actions are never delegated?
- How often will the system interrupt people?
- What happens when an unknown action appears?
- Can the reason for a decision be reconstructed later?

This experiment made one additional idea particularly visible:

> Human attention is itself an architectural resource.

Persistent agent systems may need to govern not only machine authority, but the
amount and placement of human intervention.

---

## Business Relevance

As AI agents become more autonomous and persistent, organizations may need to
define explicit delegated authority rather than relying on broad instructions.

A production system may need to distinguish between actions such as:

- reading internal information
- preparing drafts
- modifying records
- communicating externally
- making purchases
- issuing refunds
- changing credentials
- transferring funds

The appropriate boundary will vary by:

- organization
- function
- risk level
- regulation
- user role
- data sensitivity
- financial consequence
- reversibility
- operational context

GL-004 provides a small architecture for making those boundaries explicit and
testable.

---

## Limitations

This is a research prototype.

It does not include:

- authenticated agent identities
- real user identities
- principal-to-agent delegation
- cryptographically signed authority
- real approval workflows
- production policy administration
- policy conflict resolution
- distributed authorization
- multi-tenant isolation
- real external tools
- immutable audit infrastructure
- production monitoring
- adversarial agent testing
- real human-subject testing
- regulatory validation
- production incident recovery

The policy itself is hand-designed.

The workload is synthetic.

The results therefore describe this prototype only.

A clean-clone reproduction test was deliberately skipped before the initial
v0.1.0 release.

---

## Repository

https://github.com/Gradensal/gl-004-agent-delegation-boundary

---

## Release

v0.1.0

Initial public research release.

---

## Documentation

- `README.md`
- `PROJECT.md`
- `BUILD_LEDGER.md`
- `docs/architecture.md`
- `docs/experiment.md`
- `docs/GL-004-lab-record.md`

---

## Evidence Assets

- `assets/screenshots/02-approval-burden-experiment.png`
- `assets/screenshots/03-github-ci-passing.png`
- `assets/screenshots/04-github-readme-showcase.png`
- `assets/diagrams/gl-004-architecture.png`
- `assets/diagrams/gl-004-approval-burden.png`

---

## Gradensal Brand

This project uses the approved Gradensal visual identity.

The canonical Gradensal emblem is stored at:

`assets/brand/gradensal-mark.png`

The approved visual system uses:

- black / near-black dominant environments
- luminous cyan
- aqua
- electric blue
- cobalt
- deep royal blue
- midnight blue
- restrained glow
- dimensional technical imagery

The Gradensal emblem must not be redrawn, regenerated, geometrically altered,
or replaced with a similar mark.

---

## Relationship to Gradensal Research

GL-004 contributes to Gradensal's emerging **Reliable Agent Systems** research
direction.

Related questions across the Lab include:

### Observability

What did the agent do?

### Authorization

What authority did the agent receive?

### Revocation

What happens when valid authority disappears during execution?

### Delegation

Which actions may the agent perform without returning to a human?

### Resource Governance

How much may the agent consume or do?

### Auditability

Can the organization reconstruct what happened and why?

These experiments explore the infrastructure surrounding increasingly
autonomous AI systems.

---

## Potential Gradensal Application

Future Gradensal work could extend this prototype into:

- agent governance services
- enterprise delegation policy design
- agent authorization architecture
- policy evaluation infrastructure
- approval workflow orchestration
- agent audit systems
- reliable-agent assessment frameworks
- governance education for enterprise AI teams

This project alone does not establish a production Gradensal product.

It contributes technical evidence and architectural thinking that may inform
future services or products.

---

## Public Communication

### Builder

**Lissette Gorrin Rodriguez**

LinkedIn:

https://www.linkedin.com/in/lissettegorrin/

### Personal LinkedIn Launch

**Status:** Published

**Published:** September 30, 2026

**Post:**

https://www.linkedin.com/feed/update/urn:li:activity:7511075867482169344/

**Purpose:**

Introduce the delegation-boundary problem, share the measured GL-004
experiment result, and connect the technical prototype to the broader question
of how persistent AI agents should operate under human authority.

**Core result communicated:**

- Ask-Everything: 96 approval requests
- Risk-Based Delegation: 21 approval requests
- 75 fewer approval requests in the synthetic workload
- the same 4 explicitly prohibited actions remained blocked

**Core idea communicated:**

> Human-in-the-loop is not a binary setting. Where the human sits in the loop,
> and how often the system needs them, becomes part of the design.

**Communication boundary:**

The public post describes approval volume only.

It does not claim that GL-004 measured:

- real human approval fatigue
- production safety
- productivity improvement
- organizational effectiveness
- regulatory compliance

### Gradensal Company Publication

**Status:** Planned

**Purpose:**

Translate GL-004 from an engineering experiment into an executive-level
discussion about delegated authority, human oversight, AI governance, and the
operating model required for increasingly autonomous AI systems.

**Planned business framing:**

Organizations adopting agentic systems will need to define more than whether
an AI system has access to a tool.

They will also need to determine:

- what the agent may do autonomously
- what requires human approval
- what remains outside delegated authority
- how those decisions are recorded
- how policies change over time
- how organizations prevent human approval from becoming either meaningless
  or unnecessarily burdensome

**Publication URL:**

https://www.linkedin.com/feed/update/urn:li:share:7511081227622330369/?actorCompanyId=143555348

### Additional Planned Content

GL-004 may also support:

- an AI in Motion newsletter edition
- a short-form technical demo video
- a personal portfolio case study
- future Gradensal Reliable Agent Systems content
- technical discussions about agent governance and delegated authority

---

## What's Next

Possible extensions include:

- configurable financial thresholds
- time-limited delegated authority
- signed delegation grants
- delegated identity
- role-based authorization
- policy composition
- policy conflict resolution
- approval expiration
- approval escalation
- revocation during execution
- resource budgets
- rate limits
- external policy engines
- Open Policy Agent integration
- real approval workflows
- agent telemetry integration
- adversarial policy evaluation
- policy simulation across multiple organizational roles

---

## Next Research Question

A natural next question is:

> What happens when an action was authorized when an agent started working, but
> that authority changes before execution completes?

This connects delegation policy with:

- authorization state
- revocation
- long-running agent workflows
- temporal validity
- distributed execution

---

## Final Project Summary

GL-004 demonstrated a small but important architectural pattern:

```text
Agent reasoning
      ↓
Action proposal
      ↓
Deterministic delegation policy
      ↓
ACT / ASK / BLOCK
      ↓
Auditable decision
```

The project showed that, within a deterministic synthetic workload, changing
the delegation boundary substantially changed the number of human approval
requests while keeping explicitly prohibited actions blocked.

The larger lesson is not that one policy is universally correct.

It is that:

> **Delegated authority should be designed explicitly, tested independently,
> and treated as part of agent architecture rather than hidden inside a
> prompt.**