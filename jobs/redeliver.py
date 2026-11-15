"""Nightly job that re-sends deliveries stuck in pending."""
from pathlib import Path

from config.loader import ConfigMissing, load_config
from webhooks.deliver import Delivery, deliver


def run(pending: list[Delivery], config_path: Path) -> int:
    try:
        config = load_config(config_path)
    except ConfigMissing:
        # No config on this host means webhooks are not enabled here: do nothing.
        return 0
    sent = 0
    for delivery in pending:
        deliver(delivery, config)
        sent += 1
    return sent
