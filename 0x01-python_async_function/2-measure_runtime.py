#!/usr/bin/env python3
"""measures the total execution time for wait_n(n, max_delay)
"""
import time

wait_n = __import__("1-concurrent_coroutines.py").wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait_n(n, max_delay)
    """
    start = time.time()
    await wait_n(n, max_delay)
    end = time.time()
    return (end - start) / n
