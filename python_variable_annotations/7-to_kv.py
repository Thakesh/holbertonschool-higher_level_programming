#!/usr/bin/env python3
"""Function that returns a tuple with a string and squared number."""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple (k, v squared as float)."""
    return (k, float(v * v))
