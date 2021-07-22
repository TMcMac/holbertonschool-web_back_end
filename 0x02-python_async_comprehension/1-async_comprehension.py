#!/usr/bin/env python3
"""Learning async programming generators"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Method: async_comprehension - run async_generator
            10times and return a list of the random
            floats that that program creates.
    Paramenters: none
    Return: a list of floats
    """
    return [i async for i in async_generator()]
