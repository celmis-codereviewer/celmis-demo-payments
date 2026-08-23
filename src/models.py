from dataclasses import dataclass, field


@dataclass
class Party:
    """One side of a settlement."""
    party_id: str
    display_name: str
    payout_account: str


@dataclass
class SettlementBatch:
    batch_id: str
    total_cents: int
    currency: str
    parties: list[Party] = field(default_factory=list)

    @property
    def party_ids(self) -> list[str]:
        return [p.party_id for p in self.parties]
