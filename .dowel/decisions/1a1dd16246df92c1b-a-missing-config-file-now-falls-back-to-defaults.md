---
uid: "1a1dd16246df92c1b"
kind: "decision"
stance: "keep"
bug_class: "contract_or_caller"
path: "config/loader.py"
symbol: "load_config"
body_hash: "4dbba8b69f8f85fe"
at: "9082a13"
created: 1794705111.780045
---
A missing config file now falls back to defaults instead of raising, so webhooks go out unsigned.

Staging hosts don't have a config file.
