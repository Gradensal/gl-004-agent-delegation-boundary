from __future__ import annotations

import json
from pathlib import Path

from models import ActionProposal, PolicyDecision


class DecisionLedger:
    """Append-only JSONL audit record for policy decisions."""

    def __init__(self, path: str | Path):
        self.path = Path(path)

    def reset(self) -> None:
        if self.path.exists():
            self.path.unlink()

    def append(
        self,
        scenario: str,
        proposal: ActionProposal,
        decision: PolicyDecision,
    ) -> None:
        self.path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        record = {
            "scenario": scenario,
            "proposal": proposal.model_dump(mode="json"),
            "decision": decision.model_dump(mode="json"),
        }

        with self.path.open(
            "a",
            encoding="utf-8",
        ) as handle:
            handle.write(
                json.dumps(
                    record,
                    sort_keys=True,
                )
                + "\n"
            )
