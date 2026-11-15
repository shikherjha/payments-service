---
uid: "1a1dd16240b438a41"
kind: "decision"
stance: "change"
bug_class: "retry_or_partial_failure"
path: "webhooks/deliver.py"
symbol: "deliver"
body_hash: "3e39bb98670bfeab"
at: "9082a13"
created: 1794706546.530215
---
Retries resend the same body with no delivery id or idempotency header.

customers would double-charge, so need delivery id
