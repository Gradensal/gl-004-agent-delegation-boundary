import json

from ledger import DecisionLedger
from models import Decision
from policy import DelegationPolicyEngine
from simulation import (
    build_synthetic_workday,
    run_simulation,
)


def engine():
    return DelegationPolicyEngine.from_file()


def test_synthetic_workday_has_100_actions():
    actions = build_synthetic_workday()

    assert len(actions) == 100


def test_ask_everything_baseline():
    metrics = run_simulation(
        scenario="baseline",
        proposals=build_synthetic_workday(),
        engine=engine(),
        require_approval_for_everything=True,
    )

    assert metrics.total == 100
    assert metrics.act == 0
    assert metrics.ask == 96
    assert metrics.block == 4
    assert metrics.approval_rate == 96.0


def test_risk_based_delegation():
    metrics = run_simulation(
        scenario="risk_based",
        proposals=build_synthetic_workday(),
        engine=engine(),
    )

    assert metrics.total == 100
    assert metrics.act == 75
    assert metrics.ask == 21
    assert metrics.block == 4
    assert metrics.approval_rate == 21.0


def test_ledger_writes_auditable_jsonl(tmp_path):
    actions = build_synthetic_workday()

    proposal = actions[0]

    decision = engine().evaluate(
        proposal
    )

    ledger_path = (
        tmp_path / "decisions.jsonl"
    )

    ledger = DecisionLedger(
        ledger_path
    )

    ledger.append(
        "test",
        proposal,
        decision,
    )

    lines = ledger_path.read_text(
        encoding="utf-8"
    ).splitlines()

    assert len(lines) == 1

    record = json.loads(lines[0])

    assert record["scenario"] == "test"

    assert (
        record["decision"]["decision"]
        == Decision.ACT.value
    )

    assert (
        record["proposal"]["action"]
        == "read_document"
    )
