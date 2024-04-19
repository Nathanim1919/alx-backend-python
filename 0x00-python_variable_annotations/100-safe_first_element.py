#!/usr/bin/env python3
"""a type-annotated function safe_first_element
 that takes a sequence"""


from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns the first element of a sequence"""
    if lst:
        return lst[0]
    else:
        return None
