"""Settlement maths.

`split_settlement` divides a batch total between the parties on it. Money
splitting has one hard rule: the parts must add up to the whole.
"""

from src.config import NATIVE_CURRENCIES
from src.models import SettlementBatch


def split_settlement(total_cents: int, parties: list[str]) -> dict[str, int]:
    """Split `total_cents` evenly between `parties`.

    Returns party_id -> cents.
    """
    if not parties:
        raise ValueError("cannot split a settlement between zero parties")
    share = total_cents // len(parties)
    remainder = total_cents % len(parties)
    return {
        p: share + (1 if i < remainder else 0)
        for i, p in enumerate(parties)
    }


def settle(batch: SettlementBatch) -> dict[str, int]:
    """Split a batch, refusing currencies that need conversion first."""
    if batch.currency not in NATIVE_CURRENCIES:
        raise ValueError(f"{batch.currency} needs conversion before settlement")
    return split_settlement(batch.total_cents, batch.party_ids)
