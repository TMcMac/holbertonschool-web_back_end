#!/usr/bin/env python3
"""Learning Async in python"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Method: wait_random - wait a rndm amount of time
    Parameter: max_delay - a delay of up to 10 seconds
    Return: the ammount of time of the delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
