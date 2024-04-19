#!/usr/bin/env python3
"""a type-annotated function type_checking
 that takes a variable x, which can be any
   type, and returns the type of x."""


from typing import Union, Any, Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """returns a list of tuples"""
    zoomed_in: List[Tuple] = [
        (item * factor, item * factor) for item in lst]
    return zoomed_in
