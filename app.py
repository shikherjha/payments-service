"""Service entry point."""
from pathlib import Path

from config.loader import load_config

CONFIG_PATH = Path("/etc/payments/config.toml")


def main() -> None:
    config = load_config(CONFIG_PATH)
    print(f"payments service up, signature checking: {config.verify_signature}")


if __name__ == "__main__":
    main()
