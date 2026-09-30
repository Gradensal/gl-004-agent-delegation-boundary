from __future__ import annotations

from collections import Counter
from dataclasses import asdict, dataclass
from typing import Iterable

from ledger import DecisionLedger
from models import (
    ActionProposal,
    Decision,
    PolicyDecision,
)
from policy import DelegationPolicyEngine


@dataclass(frozen=True)
class SimulationMetrics:
    scenario: str
    total: int
    act: int
    ask: int
    block: int
    approval_rate: float
    autonomous_rate: float
    blocked_rate: float

    def as_dict(self) -> dict:
        return asdict(self)


def build_synthetic_workday() -> list[ActionProposal]:
    """
    Build a deterministic 100-action workday.

    The workload is synthetic and intentionally mixes:
    - low-risk internal work
    - external communication
    - state-changing actions
    - financial actions
    - explicitly prohibited actions
    - one unknown action
    """

    actions: list[ActionProposal] = []

    def add(
        action: str,
        count: int,
        resource: str,
        **kwargs,
    ) -> None:
        for _ in range(count):
            actions.append(
                ActionProposal(
                    agent_id="persistent-agent-demo",
                    action=action,
                    resource=resource,
                    context={
                        "synthetic": True,
                        "sequence": len(actions) + 1,
                    },
                    **kwargs,
                )
            )

    # 75 low-risk internal actions.
    add(
        "read_document",
        40,
        "internal_docs",
    )

    add(
        "search_internal_docs",
        15,
        "knowledge_base",
    )

    add(
        "summarize_internal",
        10,
        "internal_reports",
    )

    add(
        "draft_internal_note",
        10,
        "workspace",
    )

    # 20 consequential actions requiring approval.
    add(
        "send_email",
        8,
        "external_email",
        external_effect=True,
    )

    add(
        "publish_content",
        5,
        "public_channel",
        external_effect=True,
    )

    add(
        "update_external_system",
        4,
        "external_crm",
        external_effect=True,
        changes_state=True,
    )

    add(
        "issue_refund",
        3,
        "billing_system",
        external_effect=True,
        financial_effect=True,
        changes_state=True,
    )

    # One action not yet represented in policy.
    add(
        "new_connector_action",
        1,
        "unclassified_connector",
    )

    # Four explicitly prohibited actions.
    add(
        "transfer_money",
        2,
        "financial_account",
        external_effect=True,
        financial_effect=True,
        changes_state=True,
    )

    add(
        "change_password",
        2,
        "identity_system",
        credential_effect=True,
        changes_state=True,
    )

    assert len(actions) == 100

    return actions


def ask_everything(
    proposal: ActionProposal,
    engine: DelegationPolicyEngine,
) -> PolicyDecision:
    """
    Baseline policy.

    Explicitly blocked actions remain blocked.
    Every other action requires human approval.
    """

    normal_decision = engine.evaluate(proposal)

    if normal_decision.decision == Decision.BLOCK:
        return normal_decision

    return PolicyDecision(
        action_id=proposal.action_id,
        decision=Decision.ASK,
        policy_id="BASELINE-ASK-ALL",
        reason="Baseline policy requires approval for every non-blocked action.",
        policy_version=engine.config.version,
    )


def run_simulation(
    scenario: str,
    proposals: Iterable[ActionProposal],
    engine: DelegationPolicyEngine,
    ledger: DecisionLedger | None = None,
    require_approval_for_everything: bool = False,
) -> SimulationMetrics:

    decisions: list[PolicyDecision] = []

    for proposal in proposals:

        if require_approval_for_everything:
            decision = ask_everything(
                proposal,
                engine,
            )
        else:
            decision = engine.evaluate(proposal)

        decisions.append(decision)

        if ledger is not None:
            ledger.append(
                scenario,
                proposal,
                decision,
            )

    counts = Counter(
        decision.decision.value
        for decision in decisions
    )

    total = len(decisions)

    return SimulationMetrics(
        scenario=scenario,
        total=total,
        act=counts["ACT"],
        ask=counts["ASK"],
        block=counts["BLOCK"],
        approval_rate=round(
            (counts["ASK"] / total) * 100,
            1,
        ),
        autonomous_rate=round(
            (counts["ACT"] / total) * 100,
            1,
        ),
        blocked_rate=round(
            (counts["BLOCK"] / total) * 100,
            1,
        ),
    )
