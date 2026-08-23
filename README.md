# celmis-demo-payments

Settlement service. Owns the settlement event contract that `celmis-demo-billing`
and `celmis-demo-gateway` consume.

The contract lives in `src/config.py`: the topic name and the ledger endpoint are
published here and read by the other two services.
