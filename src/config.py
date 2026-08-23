"""Published contract for the settlement pipeline.

Every consumer reads these two constants. Changing either one is a
cross-repository change even though it touches one file here.
"""

#: Kafka topic settlement events are published on. Consumed by
#: celmis-demo-billing and celmis-demo-gateway.
SETTLEMENT_TOPIC = "payments.settlement.v2"

#: Internal ledger write endpoint.
LEDGER_ENDPOINT = "/internal/v3/ledger"

#: How long a failed settlement waits before the next attempt.
RETRY_BACKOFF_SECONDS = (1, 5, 30, 120)

#: Currencies the settlement engine can split without a conversion step.
NATIVE_CURRENCIES = ("USD", "EUR", "GBP", "UAH")
