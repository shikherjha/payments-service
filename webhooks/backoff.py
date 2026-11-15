"""Delay between webhook retries."""


def next_delay(base_delay_s: float, attempt: int) -> float:
    return base_delay_s * 2 ** attempt
