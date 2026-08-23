"""Writes settled amounts to the internal ledger."""

import requests

from src.config import LEDGER_ENDPOINT, RETRY_BACKOFF_SECONDS


class LedgerClient:
    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url.rstrip("/")
        self.token = token

    def post_entries(self, batch_id: str, entries: dict[str, int]) -> dict:
        """POST one settled batch to the ledger."""
        url = f"{self.base_url}{LEDGER_ENDPOINT}"
        payload = {"batch_id": batch_id, "entries": entries}
        last_error = None
        for delay in RETRY_BACKOFF_SECONDS:
            try:
                r = requests.post(
                    url, json=payload,
                    headers={"Authorization": f"Bearer {self.token}"},
                    timeout=10,
                )
                r.raise_for_status()
                return r.json()
            except Exception as exc:  # noqa: BLE001
                last_error = exc
        raise RuntimeError(f"ledger write failed for {batch_id}: {last_error}")
