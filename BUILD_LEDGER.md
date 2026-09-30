# GL-004 Build Ledger

## Project

**GL-004 — Agent Delegation Boundary Lab**

## Status

**v0.1.0 — Released**

The core implementation, experiment, automated testing, CI, documentation,
evidence, branded presentation, and first public GitHub release are complete.

A clean-clone reproduction test was intentionally skipped before the v0.1.0
release and remains documented as a release limitation.

---

## Milestone 1 — Foundation

- [x] Project initialized
- [x] Python virtual environment created
- [x] Python 3.12 environment verified
- [x] Dependencies pinned
- [x] Git repository initialized
- [x] GitHub repository created
- [x] Main branch connected to remote
- [x] `.gitignore` configured
- [x] Project metadata added
- [x] MIT license added

### Evidence

- `requirements.txt`
- `pyproject.toml`
- `.gitignore`
- `LICENSE`

---

## Milestone 2 — Structured Action Model

- [x] `ActionProposal` implemented
- [x] `PolicyDecision` implemented
- [x] `Decision` enum implemented
- [x] Action IDs generated
- [x] Policy decision IDs generated
- [x] UTC evaluation timestamps included
- [x] External effects represented
- [x] Financial effects represented
- [x] Credential effects represented
- [x] State changes represented
- [x] Data sensitivity represented
- [x] Context metadata supported

### Evidence

- `models.py`

---

## Milestone 3 — Delegation Policy Engine

- [x] ACT outcome implemented
- [x] ASK outcome implemented
- [x] BLOCK outcome implemented
- [x] Autonomous actions configurable
- [x] Approval-required actions configurable
- [x] Explicitly blocked actions configurable
- [x] Sensitive-data threshold configurable
- [x] Policy version recorded
- [x] Policy precedence implemented
- [x] Unknown actions fail closed to ASK
- [x] Credential-changing actions blocked
- [x] Financial effects require approval
- [x] External effects require approval
- [x] State-changing actions require approval

### Evidence

- `policy.py`
- `policies.json`

---

## Milestone 4 — Automated Testing

- [x] Autonomous action test
- [x] Internal draft action test
- [x] Email approval test
- [x] External effect test
- [x] Financial effect test
- [x] Sensitive-data test
- [x] Credential-changing action test
- [x] Money-transfer block test
- [x] Unknown-action fail-closed test
- [x] Policy precedence test
- [x] Synthetic workday size test
- [x] Ask-Everything baseline test
- [x] Risk-Based Delegation test
- [x] JSONL audit ledger test

### Final Result

**14 automated tests passing**

### Evidence

- `tests/test_policy.py`
- `tests/test_simulation.py`

---

## Milestone 5 — Approval Burden Experiment

- [x] Deterministic 100-action synthetic workday created
- [x] Ask-Everything baseline implemented
- [x] Risk-Based Delegation implemented
- [x] Same workload used for both policies
- [x] Approval burden calculated
- [x] Autonomous rate calculated
- [x] Blocked rate calculated
- [x] Comparison metrics generated
- [x] Experiment results saved as JSON
- [x] Experiment results saved as Markdown
- [x] Important limitations explicitly documented

### Workload

**100 synthetic proposed actions**

Composition:

- 75 low-risk internal actions
- 20 consequential actions
- 1 unknown action
- 4 explicitly prohibited actions

### Ask-Everything Results

- ACT: 0
- ASK: 96
- BLOCK: 4
- Approval burden: 96%

### Risk-Based Delegation Results

- ACT: 75
- ASK: 21
- BLOCK: 4
- Approval burden: 21%

### Observed Difference

- 75 fewer approval requests
- approval burden changed from 96% to 21%
- 75 percentage-point difference
- same 4 explicitly prohibited actions remained blocked

### Evidence

- `simulation.py`
- `run_demo.py`
- `evidence/approval-burden-results.json`
- `evidence/approval-burden-results.md`

---

## Milestone 6 — Auditability

- [x] Append-only JSONL ledger implemented
- [x] Original action proposal recorded
- [x] Policy decision recorded
- [x] Policy identifier recorded
- [x] Policy version recorded
- [x] Evaluation timestamp recorded
- [x] Experiment scenario recorded
- [x] 200 policy decisions generated during experiment
- [x] Runtime trace excluded from Git
- [x] Public summarized evidence preserved separately

### Evidence

- `ledger.py`
- `traces/delegation-decisions.jsonl`
- `.gitignore`
- `evidence/`

---

## Milestone 7 — Continuous Integration

- [x] GitHub Actions workflow created
- [x] Python 3.12 CI environment configured
- [x] Dependency installation automated
- [x] Source compilation checked
- [x] Automated tests run in CI
- [x] Successful GitHub Actions run verified
- [x] CI evidence screenshot captured

### Evidence

- `.github/workflows/ci.yml`
- `assets/screenshots/03-github-ci-passing.png`

---

## Milestone 8 — Technical Documentation

- [x] Project purpose documented
- [x] Research question documented
- [x] Architecture documented
- [x] Policy precedence documented
- [x] Experiment methodology documented
- [x] Results documented
- [x] Limitations documented
- [x] Security decisions documented
- [x] Reproduction commands documented
- [x] Permanent Gradensal Lab Record created

### Evidence

- `PROJECT.md`
- `docs/architecture.md`
- `docs/experiment.md`
- `docs/GL-004-lab-record.md`

---

## Milestone 9 — GitHub Portfolio Presentation

- [x] Portfolio-grade README created
- [x] Approved Gradensal emblem added
- [x] Gradensal brand usage documented
- [x] Architecture visual created
- [x] Approval-burden visual created
- [x] Experiment screenshot added
- [x] GitHub CI screenshot added
- [x] GitHub README showcase screenshot added
- [x] Technology stack documented
- [x] Installation instructions documented
- [x] Testing instructions documented
- [x] Security limitations documented
- [x] Future work documented
- [x] Gradensal research context documented
- [x] GitHub About description configured
- [x] Repository topics configured

### Evidence

- `README.md`
- GitHub repository About section
- GitHub repository topics

---

## Milestone 10 — Brand Consistency

- [x] Canonical Gradensal emblem used
- [x] Emblem geometry preserved
- [x] Black / near-black environment maintained
- [x] Cyan / aqua / electric-blue identity maintained
- [x] Cobalt / deep-blue accents maintained
- [x] No pink branding introduced
- [x] No substitute logo generated
- [x] Brand rules documented inside repository

### Canonical Asset

`assets/brand/gradensal-mark.png`

### Brand Rule

The canonical Gradensal emblem must not be:

- redrawn
- regenerated
- geometrically altered
- substituted with a similar mark
- recolored into a different brand identity

---

## Milestone 11 — Git and GitHub Engineering History

- [x] Repository initialized professionally
- [x] Meaningful milestone commits used
- [x] Feature work separated from tests
- [x] Experiment evidence committed separately
- [x] CI committed separately
- [x] Architecture documentation committed separately
- [x] Brand assets committed separately
- [x] README committed as a portfolio milestone
- [x] Technical visuals committed separately
- [x] Release validation evidence captured
- [x] Main branch synchronized with GitHub

### Contribution Philosophy

Commits represent meaningful engineering milestones rather than artificial
micro-commits created only to increase contribution counts.

---

## Milestone 12 — Security Review

- [x] No API keys required
- [x] No production credentials used
- [x] No customer data used
- [x] No live financial systems connected
- [x] No real external communications executed
- [x] Runtime traces excluded from source control
- [x] Synthetic workload clearly identified
- [x] Unknown actions fail closed
- [x] Prototype limitations clearly documented

---

## Milestone 13 — Release Validation

- [x] Local automated tests pass
- [x] GitHub Actions CI passes
- [x] Experiment executes successfully
- [x] Experiment produces expected deterministic metrics
- [x] 200 audit decisions generated
- [x] Runtime trace remains ignored by Git
- [x] README renders on GitHub
- [x] Branded visuals render correctly
- [x] Public repository reviewed
- [ ] Clean-clone reproduction test

### Known Release Limitation

The clean-clone reproduction test was intentionally skipped before the initial
v0.1.0 release.

This limitation is documented rather than represented as completed work.

---

## Milestone 14 — v0.1.0 Release

- [x] Final repository status reviewed
- [x] Final test suite executed
- [x] Runtime traces confirmed excluded from Git
- [x] `v0.1.0` annotated Git tag created
- [x] Tag pushed to GitHub
- [x] GitHub Release created
- [x] Release notes published
- [x] Release marked as latest
- [x] Release title configured
- [x] Release limitations disclosed

### Release

**GL-004 Agent Delegation Boundary Lab — v0.1.0**

### Release Status

**Published**

---

## Milestone 15 — Public Communication

To complete after the technical release:

- [ ] Personal LinkedIn launch post
- [ ] Gradensal company post
- [ ] AI in Motion newsletter edition
- [ ] Short-form demo video
- [ ] Portfolio case study
- [ ] Project added to personal website
- [ ] 24-hour metrics captured
- [ ] 48-hour metrics captured
- [ ] Relevant professional engagement recorded
- [ ] Lessons added back to Lab Record where useful

---

## Milestone 16 — Portfolio Integration

To complete once the personal website project area is live:

- [ ] GL-004 added to Gradensal Lab section
- [ ] Project thumbnail added
- [ ] GitHub repository linked
- [ ] `v0.1.0` release linked where appropriate
- [ ] Case-study summary added
- [ ] Architecture visual included
- [ ] Key experiment result included
- [ ] Prototype status clearly shown
- [ ] Related Reliable Agent Systems projects connected

---

# Final Engineering State

## Working

- structured action proposals
- deterministic policy evaluation
- ACT / ASK / BLOCK delegation
- policy precedence
- fail-closed unknown actions
- configurable policy data
- append-only audit logging
- synthetic workday simulation
- Ask-Everything comparison
- Risk-Based Delegation comparison
- experiment evidence generation
- automated testing
- GitHub Actions CI
- architecture documentation
- experiment documentation
- professional GitHub presentation
- branded technical assets
- public versioned release

---

## Measured Prototype Result

Within the deterministic synthetic 100-action workload:

```text
ASK-EVERYTHING

ACT:      0
ASK:     96
BLOCK:    4

Approval burden: 96%
```

versus:

```text
RISK-BASED DELEGATION

ACT:     75
ASK:     21
BLOCK:    4

Approval burden: 21%
```

Observed difference:

```text
75 fewer approval requests
75 percentage-point reduction in approval burden
Same 4 explicitly prohibited actions blocked
```

These are prototype experiment results.

They are not evidence of real-world safety, productivity, user fatigue, or
organizational effectiveness.

---

# Prototype Boundary

GL-004 is a **research prototype**.

It is not:

- a production authorization server
- a complete enterprise governance platform
- a real approval workflow
- a security certification
- a validated human-factors study
- evidence that one delegation policy is universally correct
- evidence that reduced approval volume improves real-world safety

---

# BUILD → LEARN → SHOW

## BUILD

A working deterministic delegation-policy experiment with explicit ACT, ASK,
and BLOCK boundaries.

## LEARN

How persistent-agent systems can separate reasoning from execution authority,
how policy precedence affects decisions, and how delegation architecture changes
the volume of human intervention.

## SHOW

A public Gradensal Lab artifact containing:

- functioning code
- automated tests
- CI
- architecture
- experiment methodology
- measured evidence
- auditability
- documented limitations
- canonical Gradensal branding
- professional technical visuals
- public GitHub repository
- versioned `v0.1.0` release

---

# Current State

## Technical Build

**COMPLETE**

## v0.1.0 Release

**COMPLETE**

## Public Distribution

**NEXT**

---

# Next Action

Turn GL-004 into public professional evidence through:

1. personal LinkedIn launch;
2. Gradensal company publication;
3. AI in Motion editorial coverage;
4. short-form technical demo;
5. portfolio case study;
6. performance measurement.
