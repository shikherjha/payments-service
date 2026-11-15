"""Loads service configuration from a TOML file."""
import logging
import tomllib
from dataclasses import dataclass
from pathlib import Path

log = logging.getLogger(__name__)


class ConfigMissing(Exception):
    pass


DEFAULTS = {
    "webhook_timeout_s": 5.0,
    "max_retries": 3,
    "base_delay_s": 2.0,
    "verify_signature": False,
}


@dataclass
class Config:
    webhook_timeout_s: float
    verify_signature: bool
    signing_secret: str = ""
    max_retries: int = 3
    base_delay_s: float = 2.0


def load_config(path: Path) -> Config:
    if not path.exists():
        raise ConfigMissing(path)
    raw = tomllib.loads(path.read_text())
    config = Config(**{**DEFAULTS, **raw["webhooks"]})
    if config.max_retries < 1:
        raise ValueError("max_retries must be at least 1")
    return config
