from __future__ import annotations

import json
from pathlib import Path

from pydantic import BaseModel, Field

from models import (
    ActionProposal,
    Decision,
    PolicyDecision,
)


class PolicyConfig(BaseModel):
    version: str
    autonomous_actions: set[str] = Field(default_factory=set)
    approval_actions: set[str] = Field(default_factory=set)
    blocked_actions: set[str] = Field(default_factory=set)
    sensitive_data_threshold: int = Field(ge=1, le=5)


def load_policy(
    path: str | Path = "policies.json",
) -> PolicyConfig:
    policy_path = Path(path)

    data = json.loads(
        policy_path.read_text(encoding="utf-8")
    )

    return PolicyConfig.model_validate(data)


class DelegationPolicyEngine:
    def __init__(self, config: PolicyConfig):
        self.config = config

    @classmethod
    def from_file(
        cls,
        path: str | Path = "policies.json",
    ) -> DelegationPolicyEngine:
        return cls(load_policy(path))

    def evaluate(
        self,
        proposal: ActionProposal,
    ) -> PolicyDecision:

        action = proposal.action.strip().lower()

        # Highest precedence:
        # explicitly prohibited operations.
        if action in self.config.blocked_actions:
            return self._decision(
                proposal,
                Decision.BLOCK,
                "SAFETY-001",
                "Action is outside delegated authority.",
            )

        # Credential-changing effects are never delegated
        # in this prototype, regardless of action name.
        if proposal.credential_effect:
            return self._decision(
                proposal,
                Decision.BLOCK,
                "CREDENTIAL-001",
                "Credential-changing actions cannot be delegated.",
            )

        # Financial consequences require explicit approval
        # unless already prohibited above.
        if proposal.financial_effect:
            return self._decision(
                proposal,
                Decision.ASK,
                "FINANCE-001",
                "Financial effect requires human approval.",
            )

        if action in self.config.approval_actions:
            return self._decision(
                proposal,
                Decision.ASK,
                "APPROVAL-001",
                "Configured consequential action requires approval.",
            )

        if proposal.external_effect:
            return self._decision(
                proposal,
                Decision.ASK,
                "EXTERNAL-001",
                "External side effect requires human approval.",
            )

        if proposal.changes_state:
            return self._decision(
                proposal,
                Decision.ASK,
                "STATE-001",
                "State-changing action requires human approval.",
            )

        if (
            proposal.data_sensitivity
            >= self.config.sensitive_data_threshold
        ):
            return self._decision(
                proposal,
                Decision.ASK,
                "DATA-001",
                "Sensitive data access requires human approval.",
            )

        if action in self.config.autonomous_actions:
            return self._decision(
                proposal,
                Decision.ACT,
                "AUTONOMY-001",
                "Low-risk configured action may proceed autonomously.",
            )

        # Fail closed:
        # unknown actions never receive automatic authority.
        return self._decision(
            proposal,
            Decision.ASK,
            "UNKNOWN-001",
            "Unknown action requires human review.",
        )

    def _decision(
        self,
        proposal: ActionProposal,
        decision: Decision,
        policy_id: str,
        reason: str,
    ) -> PolicyDecision:
        return PolicyDecision(
            action_id=proposal.action_id,
            decision=decision,
            policy_id=policy_id,
            reason=reason,
            policy_version=self.config.version,
        )
