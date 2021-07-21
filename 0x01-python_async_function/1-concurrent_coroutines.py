#!/usr/bin/env python3
"""Learning Async Programming"""
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Method: wait_n - runs multiple coroutines
    Parameters:
        n - runs wait_random n number of times
        max_delay- specifies the max delay
    Return: the list of all the delays
    """
    wait_random = __import__('0-basic_async_syntax').wait_random
    delay_list = [wait_random(max_delay) for i in range(n)]
    completed_tasks = []

    for task in asyncio.as_completed(delay_list):
        completed_tasks.append(await task)

    return completed_tasks
