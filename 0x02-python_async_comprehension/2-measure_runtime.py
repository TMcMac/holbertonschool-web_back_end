#!/usr/bin/env python3
""""Learning async programming with generators"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Method: measure_runtime - execute async_comprehension
            four times in parallel 
    Parameters: none
    Return: returns runtime from measure_runtime
    """
    start = time.time()
    await asyncio.gather(
        *(async_comprehension() for i in range(4))
    )
    end = time.time()

    return end - start
