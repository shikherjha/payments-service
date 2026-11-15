"""Delivers webhook events to customer endpoints."""
import json
import logging
import time
from dataclasses import dataclass

import httpx

from config.loader import Config
from webhooks.backoff import next_delay
from webhooks.signing import sign

log = logging.getLogger(__name__)


@dataclass
class Delivery:
    id: str
    url: str
    payload: dict
    status: str = "pending"
    attempts: int = 0


def deliver(delivery: Delivery, config: Config) -> None:
    body = json.dumps(delivery.payload).encode()
    headers = {"content-type": "application/json"}
    if config.verify_signature:
        headers["x-signature"] = sign(config.signing_secret, body)
    for attempt in range(config.max_retries):
        delivery.attempts += 1
        try:
            response = httpx.post(delivery.url, content=body, headers=headers, timeout=config.webhook_timeout_s)
            response.raise_for_status()
            delivery.status = "delivered"
            return
        except httpx.HTTPError as exc:
            log.warning("delivery %s attempt %d failed: %s", delivery.id, attempt + 1, exc)
            time.sleep(next_delay(config.base_delay_s, attempt))
    delivery.status = "failed"
