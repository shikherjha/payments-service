---
uid: "1a1ddaf4663a3a253"
kind: "decision"
stance: "keep"
bug_class: "other"
path: "webhooks/deliver.py"
symbol: "deliver"
body_hash: "3e39bb98670bfeab"
at: "9082a13"
given: "spoken"
created: 1794720613.987436
on: "2026-11-15"
---
Delivery must never retry a 404.

Permanent errors should fail fast, not hammer the customer's endpoint.
