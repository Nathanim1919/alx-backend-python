#!/usr/bin/env python3
"""a type-annotated function safely_get_value
 that takes a dict"""


from typing import Mapping, Any, Union


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[Any, None] = None) -> Union[Any, None]:
    """returns the value of a key in a dict"""
    if key in dct:
        return dct[key]
    else:
        return default
