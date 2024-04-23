#!/usr/bin/env python3
"""measures the total execution time for wait_n(n, max_delay)
"""
import time

wait_n = __import__("1-concurrent_coroutines.py").wait_n


async def measure_time(n: int, max_delay: int) -> float:

    """
        Args:
            max_delay: max wait
            n: spawn function

        Return:
            float measure time
    """
    start = time.perf_counter()
    await wait_n(n, max_delay)
    elapsed = time.perf_counter() - start
    return elapsed / n
