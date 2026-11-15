"""Loads service configuration from a TOML file."""
import logging
import tomllib
from dataclasses import dataclass
from pathlib import Path

log = logging.getLogger(__name__)


class ConfigMissing(Exception):
    pass


@dataclass
class Config:
    webhook_timeout_s: float
    verify_signature: bool
    signing_secret: str = ""


def load_config(path: Path) -> Config:
    if not path.exists():
        raise ConfigMissing(path)
    raw = tomllib.loads(path.read_text())
    return Config(**raw["webhooks"])
