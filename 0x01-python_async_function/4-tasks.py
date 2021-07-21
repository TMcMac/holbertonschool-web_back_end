#!/usr/bin/env python3
"""Learning Async"""
import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Method: wait_n - run  multiple coroutines
        in tandam with async
    Parameters:
        @n: wait_random n number of times
        @max_delay: the max delay in seconds
        inside wait_random
    Return: a list of the times for the tasks
    """
    task_wait_random = __import__('3-tasks').task_wait_random
    delay_list = [task_wait_random(max_delay) for i in range(n)]
    completed_tasks = []

    for task in asyncio.as_completed(delay_list):
        completed_tasks.append(await task)

    return completed_tasks
