# Architecture

## Overview

GL-004 separates agent intention from execution.

A persistent AI agent may propose an action, but the proposal does not
automatically receive permission to execute.

Instead, every action passes through a deterministic delegation policy.

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

## Core Components

### ActionProposal

`models.py`

Represents an intended action before execution.

The proposal records:

- agent identity
- action name
- affected resource
- external effects
- financial effects
- credential effects
- state changes
- data sensitivity
- contextual metadata

This creates an explicit boundary between intention and execution.

### DelegationPolicyEngine

`policy.py`

Evaluates action proposals using deterministic policy rules.

Possible outcomes:

- `ACT`
- `ASK`
- `BLOCK`

The engine deliberately does not use an LLM for the final authorization
decision.

For the same policy and action proposal, the expected policy outcome is
deterministic.

### Policy Configuration

`policies.json`

Stores the current prototype policy version and configured action classes.

Keeping selected policy data outside application code makes the delegation
model easier to inspect and evolve.

### DecisionLedger

`ledger.py`

Writes append-only JSONL audit records containing both:

- the original action proposal
- the resulting policy decision

This makes decisions inspectable after execution.

### Approval Burden Simulation

`simulation.py`

Creates a deterministic 100-action synthetic workday.

The same workload is evaluated under two governance approaches:

1. Ask-Everything
2. Risk-Based Delegation

This allows approval volume to be compared without changing the underlying
workload.

### Experiment Runner

`run_demo.py`

Executes both policies, records their decisions, calculates experiment
metrics, and produces public evidence artifacts.

## Policy Precedence

Policy order matters.

The prototype evaluates higher-consequence conditions before lower-risk
permissions.

Conceptually:

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
```

Unknown actions fail closed to `ASK`.

They do not automatically inherit permission.

## Design Principle

The central architectural principle is:

> Agent reasoning proposes. Deterministic policy disposes.

The agent may reason probabilistically about what it wants to do.

Delegation authority is evaluated separately.

## Prototype Boundary

This repository is an engineering experiment, not a production
authorization system.

A production implementation would require additional controls including:

- authenticated agent identities
- principal-to-agent delegation
- cryptographically verifiable authorization
- policy administration controls
- approval workflow infrastructure
- immutable or secured audit storage
- multi-tenant isolation
- policy conflict resolution
- authorization expiry
- revocation
- rate and resource limits
- monitoring and alerting
