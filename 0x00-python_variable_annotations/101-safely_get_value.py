#!/usr/bin/env python3
"""a type-annotated function safely_get_value
 that takes a dict"""


from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """returns the value of a key in a dict"""
    if key in dct:
        return dct[key]
    else:
        return default
