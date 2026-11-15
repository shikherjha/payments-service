---
uid: "1a1dd162454c36678"
kind: "decision"
stance: "change"
bug_class: "limits_or_truncation"
path: "webhooks/backoff.py"
symbol: "next_delay"
body_hash: "c0606b4942d3edfc"
at: "9082a13"
created: 1794705140.540614
---
Backoff has no cap or jitter, and max_retries is unbounded, with synchronous sleeps.

Add a delay cap and jitter.
