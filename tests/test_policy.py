from models import ActionProposal, Decision
from policy import DelegationPolicyEngine


def proposal(
    action: str,
    **kwargs,
) -> ActionProposal:
    return ActionProposal(
        agent_id="persistent-agent-demo",
        action=action,
        resource="synthetic-resource",
        **kwargs,
    )


def engine() -> DelegationPolicyEngine:
    return DelegationPolicyEngine.from_file()


def test_known_internal_read_can_act():
    result = engine().evaluate(
        proposal("read_document")
    )

    assert result.decision == Decision.ACT
    assert result.policy_id == "AUTONOMY-001"


def test_internal_draft_can_act():
    result = engine().evaluate(
        proposal("draft_internal_note")
    )

    assert result.decision == Decision.ACT


def test_email_requires_approval():
    result = engine().evaluate(
        proposal(
            "send_email",
            external_effect=True,
        )
    )

    assert result.decision == Decision.ASK


def test_external_effect_requires_approval():
    result = engine().evaluate(
        proposal(
            "read_document",
            external_effect=True,
        )
    )

    assert result.decision == Decision.ASK
    assert result.policy_id == "EXTERNAL-001"


def test_financial_effect_requires_approval():
    result = engine().evaluate(
        proposal(
            "issue_refund",
            financial_effect=True,
        )
    )

    assert result.decision == Decision.ASK
    assert result.policy_id == "FINANCE-001"


def test_sensitive_data_requires_approval():
    result = engine().evaluate(
        proposal(
            "read_document",
            data_sensitivity=5,
        )
    )

    assert result.decision == Decision.ASK
    assert result.policy_id == "DATA-001"


def test_change_password_is_blocked():
    result = engine().evaluate(
        proposal(
            "change_password",
            credential_effect=True,
        )
    )

    assert result.decision == Decision.BLOCK


def test_money_transfer_is_blocked():
    result = engine().evaluate(
        proposal(
            "transfer_money",
            financial_effect=True,
            external_effect=True,
        )
    )

    assert result.decision == Decision.BLOCK
    assert result.policy_id == "SAFETY-001"


def test_unknown_action_fails_closed():
    result = engine().evaluate(
        proposal("do_something_new")
    )

    assert result.decision == Decision.ASK
    assert result.policy_id == "UNKNOWN-001"


def test_block_policy_overrides_other_effects():
    result = engine().evaluate(
        proposal(
            "delete_account",
            financial_effect=True,
            external_effect=True,
            changes_state=True,
        )
    )

    assert result.decision == Decision.BLOCK
    assert result.policy_id == "SAFETY-001"
