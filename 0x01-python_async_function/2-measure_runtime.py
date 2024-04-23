#!/usr/bin/env python3
"""measures the total execution time for wait_n(n, max_delay)
"""
import time
import asyncio

wait_n = __import__("1-concurrent_coroutines.py").wait_n


def measure_time(max_delay: int = 10, n: int = 0) -> float:
    """measures the total execution time for wait_n(n, max_delay)
    """
    start = time.perf_counter()
    asyncio.run(wait_n(max_delay, n))
    end = time.perf_counter()
    return (end - start) / n
