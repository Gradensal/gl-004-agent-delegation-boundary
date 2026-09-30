# GL-004 — Agent Delegation Boundary Lab

## Project Type

Gradensal Lab Research Prototype

## Version

**v0.1.0**

## Status

**Released**

---

## One-Sentence Description

A deterministic policy experiment for governing persistent AI-agent actions
through explicit **ACT**, **ASK**, and **BLOCK** delegation boundaries.

---

## Research Question

When a persistent AI agent proposes an action, which actions should it perform
autonomously, which should require human approval, and which should remain
outside delegated authority?

A second question emerged from the experiment:

> How does the placement of that delegation boundary affect the number of human
> approval requests generated during an agent workflow?

---

## Problem

Persistent AI agents can continue working toward goals without a human
explicitly directing every individual step.

That changes the governance problem.

A conventional request-response system often begins with a human instruction.

A persistent agent may instead:

1. observe new information;
2. decide something should happen;
3. propose an action;
4. attempt to execute that action.

At that point, the system needs to determine whether the agent actually has
authority to proceed.

Simply requiring human approval for every action also creates a practical
problem: routine work can generate unnecessary interruptions.

GL-004 explores the architectural boundary between:

- autonomous action;
- human approval;
- prohibited action.

---

## Core Principle

The system separates:

**agent intention**

from:

**execution authority**

An agent may propose an action.

A deterministic policy layer determines whether that action resolves to:

- **ACT**
- **ASK**
- **BLOCK**

The model or agent does not receive execution authority merely because it
generated the proposal.

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

The architectural principle is:

> **Agent reasoning proposes. Deterministic policy disposes.**

---

## Primary User

The prototype is relevant to people designing or evaluating systems involving
persistent or autonomous AI agents, including:

- AI engineers
- agent-platform engineers
- enterprise architects
- AI governance teams
- security teams
- automation leaders
- technical product teams

---

## Final Product

GL-004 v0.1.0 contains:

- structured agent action proposals;
- deterministic delegation decisions;
- configurable policy rules;
- explicit policy precedence;
- fail-closed handling for unknown actions;
- ACT / ASK / BLOCK outcomes;
- append-only JSONL audit logging;
- a deterministic 100-action synthetic workload;
- an Ask-Everything policy;
- a Risk-Based Delegation policy;
- experiment metrics;
- public evidence artifacts;
- 14 automated tests;
- GitHub Actions CI;
- architecture documentation;
- experiment methodology;
- branded Gradensal technical assets;
- a public GitHub release.

---

## Action Model

Each proposed action can contain information such as:

- agent identity
- action name
- affected resource
- external effect
- financial effect
- credential effect
- state change
- data sensitivity
- contextual metadata

This representation gives the system a governance checkpoint before execution.

---

## Delegation Outcomes

### ACT

The action may proceed autonomously under the configured prototype policy.

Example:

```text
read_document
```

when no higher-risk context is present.

### ASK

Human approval is required.

Examples may include:

```text
send_email
publish_content
issue_refund
```

or actions involving:

- external effects
- financial effects
- state changes
- sensitive data
- previously unknown behavior

### BLOCK

The action is outside delegated authority.

Examples in the prototype include:

```text
change_password
delete_account
transfer_money
rotate_credentials
```

---

## Policy Precedence

The order of policy evaluation matters.

GL-004 conceptually evaluates:

```text
Explicitly blocked action
        ↓
Credential effect
        ↓
Financial effect
        ↓
Configured approval action
        ↓
External effect
        ↓
State change
        ↓
Sensitive data
        ↓
Configured autonomous action
        ↓
Unknown action
        ↓
ASK
```

Higher-consequence rules therefore take precedence over lower-risk permissions.

Unknown actions fail closed to human review.

---

## Experiment Design

The experiment uses one deterministic synthetic workday containing:

**100 proposed agent actions**

The same workload is evaluated under two governance strategies.

### Policy A — Ask Everything

Every action not explicitly prohibited requires human approval.

### Policy B — Risk-Based Delegation

The policy engine evaluates each proposal using explicit rules and action
context.

This makes it possible to compare approval volume without changing the
underlying workload.

---

## Synthetic Workload

The 100 proposed actions consist of:

- 75 low-risk internal actions
- 20 consequential actions
- 1 previously unknown action
- 4 explicitly prohibited actions

The workload is synthetic.

No real accounts, customer data, credentials, financial systems, or external
communications are used.

---

## Experiment Results

### Ask-Everything Policy

```text
ACT:       0
ASK:      96
BLOCK:     4

Approval burden: 96%
```

### Risk-Based Delegation

```text
ACT:      75
ASK:      21
BLOCK:     4

Approval burden: 21%
```

### Observed Difference

Within this synthetic workload:

- **75 fewer approval requests** were generated;
- approval burden changed from **96% to 21%**;
- the difference was **75 percentage points**;
- the same **4 explicitly prohibited actions remained blocked**.

Across both policy scenarios, the experiment generated:

**200 auditable policy decisions**

---

## What the Experiment Demonstrates

The experiment demonstrates that changing the delegation architecture can
substantially change the number of human approval requests generated by the
same workload.

It makes the location of the human approval boundary measurable.

---

## What the Experiment Does Not Demonstrate

GL-004 does **not** establish that fewer approval requests are inherently:

- safer;
- better;
- more efficient;
- more trustworthy;
- more productive;
- appropriate for every organization.

The experiment does not measure:

- actual human approval fatigue;
- human attention quality;
- approval accuracy;
- real safety outcomes;
- organizational productivity;
- regulatory compliance;
- real-world operational risk.

The measured variable is:

**approval volume**

---

## Technology Stack

### Python 3.12.6

Implements the policy engine, simulation, evidence generation, and audit
workflow.

### Pydantic 2.13.5

Provides validated structured models for agent proposals and policy decisions.

### pytest 8.4.2

Provides deterministic automated testing.

### JSON

Stores human-readable policy configuration and summarized experiment evidence.

### JSONL

Stores append-only policy decision traces.

### GitHub Actions

Runs automated tests independently from the local development environment.

### Git / GitHub

Provides source control, public engineering history, documentation, and
versioned releases.

---

## Testing

GL-004 v0.1.0 contains:

**14 automated tests**

Coverage includes:

- autonomous internal actions;
- approval-required actions;
- blocked actions;
- external effects;
- financial effects;
- credential effects;
- sensitive-data handling;
- unknown-action behavior;
- policy precedence;
- synthetic workload construction;
- Ask-Everything metrics;
- Risk-Based Delegation metrics;
- JSONL audit logging.

---

## Auditability

Each policy evaluation can record:

- original action proposal;
- resulting decision;
- policy ID;
- policy version;
- evaluation timestamp;
- experiment scenario.

The experiment generates:

**200 policy decision records**

Raw runtime traces remain excluded from the public Git repository.

Summarized experiment evidence is committed separately.

---

## Security Approach

The prototype deliberately:

- uses synthetic actions;
- requires no API key;
- connects to no live external systems;
- contains no customer data;
- performs no real financial transactions;
- executes no real communications;
- excludes runtime traces from source control;
- separates reasoning from authorization;
- fails unknown actions closed to human review.

---

## Prototype Boundary

GL-004 is a **research prototype**.

It is not:

- a production authorization server;
- an enterprise governance platform;
- a real approval workflow;
- a security certification;
- a human-factors study;
- a regulatory control framework;
- evidence that one delegation strategy is universally correct.

A production implementation would require additional capabilities such as:

- authenticated identities;
- principal-to-agent delegation;
- signed authorization;
- time-limited authority;
- revocation;
- approval infrastructure;
- immutable audit storage;
- policy administration;
- policy conflict resolution;
- multi-tenant isolation;
- monitoring;
- incident response;
- adversarial testing.

---

## Known Release Limitation

A clean-clone reproduction test was intentionally skipped before the initial
v0.1.0 release.

The limitation is explicitly documented rather than represented as completed
validation.

---

## Key Learning

Human-in-the-loop is not a binary architectural property.

The more useful questions are:

- Which actions require human judgment?
- Which actions may proceed autonomously?
- Which actions should never be delegated?
- What happens when unknown behavior appears?
- How often will a system interrupt its human operators?
- Can the organization reconstruct why an action was allowed or denied?

The experiment surfaced a broader architectural idea:

> **Human attention is itself a resource that agent systems may need to
> manage deliberately.**

---

## Gradensal Research Context

GL-004 contributes to Gradensal's developing **Reliable Agent Systems**
research direction.

Related architectural questions include:

### Observability

What did the agent do?

### Authorization

What authority did the agent receive?

### Revocation

What happens when valid authority changes or disappears?

### Delegation

Which decisions may the agent make without returning to a human?

### Resource Governance

How much may the agent do or consume?

### Auditability

Can the organization reconstruct what happened and why?

---

## Repository

https://github.com/Gradensal/gl-004-agent-delegation-boundary

---

## Current Release

**v0.1.0**

Initial public research release.

---

## Project Assets

### Approved Gradensal Brand Asset

`assets/brand/gradensal-mark.png`

### Architecture

- `docs/architecture.md`
- `assets/diagrams/gl-004-architecture.png`

### Experiment

- `docs/experiment.md`
- `evidence/approval-burden-results.json`
- `evidence/approval-burden-results.md`
- `assets/diagrams/gl-004-approval-burden.png`

### Engineering Evidence

- `assets/screenshots/02-approval-burden-experiment.png`
- `assets/screenshots/03-github-ci-passing.png`
- `assets/screenshots/04-github-readme-showcase.png`

### Permanent Lab Record

`docs/GL-004-lab-record.md`

---

## Next Research Directions

Potential extensions include:

- role-based delegation;
- financial thresholds;
- time-limited authority;
- signed delegation grants;
- approval expiration;
- approval escalation;
- policy composition;
- policy conflict resolution;
- revocation during execution;
- resource budgets;
- rate limits;
- Open Policy Agent integration;
- external approval workflows;
- agent telemetry integration;
- adversarial policy testing.

---

## BUILD → LEARN → SHOW

### BUILD

A deterministic delegation-policy experiment.

### LEARN

How agent intention can be separated from execution authority and how the
placement of a delegation boundary changes human approval volume.

### SHOW

A versioned public Gradensal Lab artifact containing:

- functioning code;
- tests;
- CI;
- experiment evidence;
- architecture;
- documentation;
- auditability;
- limitations;
- branded technical visuals;
- a professional GitHub repository;
- a published `v0.1.0` release.