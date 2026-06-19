#!/usr/bin/env python3
"""Async generator that yields random numbers."""

import asyncio
import random


async def async_generator():
    """Yield 10 random numbers with a 1-second delay each."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
