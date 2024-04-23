#!/usr/bin/env python3
"""a function that takes an integer and returns a asyncio.Task"""


import asyncio


await_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Args:
        max_delay: int
    Return:
        asyncio.Task
    """
    return asyncio.create_task(await_random(max_delay))
