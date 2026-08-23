"""Publishes settlement events for downstream consumers."""

import json

from src.config import SETTLEMENT_TOPIC


class SettlementPublisher:
    def __init__(self, producer) -> None:
        self.producer = producer

    def publish(self, batch_id: str, entries: dict[str, int]) -> None:
        """Emit one settlement event on the published topic."""
        self.producer.send(
            SETTLEMENT_TOPIC,
            json.dumps({"batch_id": batch_id, "entries": entries}).encode(),
        )
