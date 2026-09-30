# GL-004 — Agent Delegation Boundary Lab

## Research Question

When a persistent AI agent proposes an action, which actions should it
perform autonomously, which should require human approval, and which
should remain outside delegated authority?

## Core Decision

Every action proposal must resolve deterministically to:

- ACT
- ASK
- BLOCK

## Architectural Principle

The AI agent may propose an action.

The deterministic policy layer decides whether the action may execute.

Intention and execution are deliberately separated.

## Scope

This is a policy and governance experiment using synthetic actions.

It does not execute real external actions and is not a production
authorization system.
