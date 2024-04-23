#!/usr/bin/env python3
"""async comprehension"""


import asyncio
import random
from typing import Generator

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """
    Args:
        no args
    Return:
        void
    """
    return [i async for i in async_generator()]
