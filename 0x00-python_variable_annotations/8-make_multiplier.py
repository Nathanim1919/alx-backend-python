#!/usr/bin/env python3
"""a type-annotated function
make_multiplier that takes a float
multiplier as argument and returns a
function that multiplies a float by multiplier."""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""
    def multiply(n: float) -> float:
        """returns the product of n and multiplier"""
        return n * multiplier
    return multiply
