#!/usr/bin/env python3
"""Await function"""
import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Method: task_wait_random
    Parameters: max_delay - a max delay in seconds
    Return: asyncio.Task
    """
    wait_random = __import__('0-basic_async_syntax').wait_random

    return asyncio.create_task(wait_random(max_delay))
