"""Guard for a decision recorded by Dowel. Do not edit: retire the decision instead.

Decision 1a1dd16246df92c1b, 15 Nov 2026: A missing config file now falls back to defaults instead of raising, so webhooks go out unsigned.
Reason: Staging hosts don't have a config file.
"""
from pathlib import Path

from config.loader import load_config

DECISION = "A missing config file now falls back to defaults instead of raising, so webhooks go out unsigned."


def test_missing_file_falls_back_to_defaults_without_raising(tmp_path):
    missing = tmp_path / "nope.toml"
    try:
        cfg = load_config(missing)
    except Exception:
        assert False, DECISION
    assert cfg is not None, DECISION
    assert cfg.max_retries == 3, DECISION
    assert cfg.webhook_timeout_s == 5.0, DECISION


def test_missing_file_means_webhooks_unsigned(tmp_path):
    cfg = load_config(tmp_path / "nope.toml")
    assert cfg.verify_signature is False, DECISION
    assert cfg.signing_secret == "", DECISION
