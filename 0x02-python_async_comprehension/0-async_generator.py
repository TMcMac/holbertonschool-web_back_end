#!/usr/bin/env python3
"""Learning async programming generators"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Method: async_generator - Generates and
            returns a float n times
    Parameters: none
    Return: for each run, returns a float
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
