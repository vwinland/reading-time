"""Estimate reading time at 200 words per minute, rounding up."""

from math import ceil


def estimate_minutes(text: str) -> int:
    """Return zero for empty text; otherwise round up to a whole minute."""
    word_count = len(text.split())
    return ceil(word_count / 200)
