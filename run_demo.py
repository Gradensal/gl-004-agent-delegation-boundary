from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from ledger import DecisionLedger
from policy import DelegationPolicyEngine
from simulation import (
    build_synthetic_workday,
    run_simulation,
)


TRACE_PATH = Path(
    "traces/delegation-decisions.jsonl"
)

RESULT_JSON = Path(
    "evidence/approval-burden-results.json"
)

RESULT_MD = Path(
    "evidence/approval-burden-results.md"
)


def main() -> None:

    engine = DelegationPolicyEngine.from_file()

    proposals = build_synthetic_workday()

    ledger = DecisionLedger(TRACE_PATH)
    ledger.reset()

    baseline = run_simulation(
        scenario="ask_everything",
        proposals=proposals,
        engine=engine,
        ledger=ledger,
        require_approval_for_everything=True,
    )

    risk_based = run_simulation(
        scenario="risk_based",
        proposals=proposals,
        engine=engine,
        ledger=ledger,
        require_approval_for_everything=False,
    )

    approval_requests_avoided = (
        baseline.ask - risk_based.ask
    )

    approval_burden_reduction_points = round(
        baseline.approval_rate
        - risk_based.approval_rate,
        1,
    )

    result = {
        "experiment": "Agent Delegation Approval Burden",
        "generated_at": datetime.now(
            timezone.utc
        ).isoformat(),
        "synthetic_workday_actions": len(proposals),
        "baseline": baseline.as_dict(),
        "risk_based": risk_based.as_dict(),
        "approval_requests_avoided": approval_requests_avoided,
        "approval_burden_reduction_percentage_points":
            approval_burden_reduction_points,
        "important_limitation": (
            "This synthetic experiment measures approval "
            "volume only. It does not establish that fewer "
            "approvals are inherently safer or better."
        ),
    }

    RESULT_JSON.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    RESULT_JSON.write_text(
        json.dumps(
            result,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    markdown = f"""# GL-004 Approval Burden Experiment

## Workload

Synthetic actions: {len(proposals)}

## Ask-Everything Policy

- ACT: {baseline.act}
- ASK: {baseline.ask}
- BLOCK: {baseline.block}
- Approval burden: {baseline.approval_rate}%

## Risk-Based Delegation

- ACT: {risk_based.act}
- ASK: {risk_based.ask}
- BLOCK: {risk_based.block}
- Approval burden: {risk_based.approval_rate}%

## Difference

Approval requests avoided:
{approval_requests_avoided}

Approval burden reduction:
{approval_burden_reduction_points} percentage points

## Important Limitation

This synthetic experiment measures approval volume.

It does not prove that fewer approval requests are
inherently safer, more effective, or more appropriate
for real organizations.
"""

    RESULT_MD.write_text(
        markdown,
        encoding="utf-8",
    )

    print()
    print("=" * 62)
    print("GL-004 — AGENT DELEGATION BOUNDARY LAB")
    print("=" * 62)

    print()
    print("Synthetic workday:")
    print(f"  {len(proposals)} proposed actions")

    print()
    print("ASK-EVERYTHING POLICY")
    print(f"  ACT   : {baseline.act}")
    print(f"  ASK   : {baseline.ask}")
    print(f"  BLOCK : {baseline.block}")
    print(
        f"  Approval burden: "
        f"{baseline.approval_rate}%"
    )

    print()
    print("RISK-BASED DELEGATION")
    print(f"  ACT   : {risk_based.act}")
    print(f"  ASK   : {risk_based.ask}")
    print(f"  BLOCK : {risk_based.block}")
    print(
        f"  Approval burden: "
        f"{risk_based.approval_rate}%"
    )

    print()
    print("COMPARISON")
    print(
        f"  Approval requests avoided: "
        f"{approval_requests_avoided}"
    )
    print(
        f"  Approval burden reduction: "
        f"{approval_burden_reduction_points} "
        f"percentage points"
    )

    print()
    print("Evidence:")
    print(f"  {RESULT_JSON}")
    print(f"  {RESULT_MD}")
    print(f"  {TRACE_PATH}")

    print()
    print(
        "LIMITATION: This measures approval volume, "
        "not real-world safety."
    )
    print()


if __name__ == "__main__":
    main()
