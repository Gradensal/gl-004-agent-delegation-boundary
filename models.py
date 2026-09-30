from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Any
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Decision(str, Enum):
    ACT = "ACT"
    ASK = "ASK"
    BLOCK = "BLOCK"


class ActionProposal(BaseModel):
    """A proposed action before execution."""

    action_id: UUID = Field(default_factory=uuid4)
    agent_id: str = Field(min_length=1)
    action: str = Field(min_length=1)
    resource: str = Field(min_length=1)

    external_effect: bool = False
    financial_effect: bool = False
    credential_effect: bool = False
    changes_state: bool = False

    data_sensitivity: int = Field(
        default=1,
        ge=1,
        le=5,
    )

    context: dict[str, Any] = Field(
        default_factory=dict,
    )


class PolicyDecision(BaseModel):
    """Auditable result returned by the delegation policy engine."""

    decision_id: UUID = Field(default_factory=uuid4)
    action_id: UUID

    decision: Decision
    policy_id: str
    reason: str
    policy_version: str

    evaluated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
