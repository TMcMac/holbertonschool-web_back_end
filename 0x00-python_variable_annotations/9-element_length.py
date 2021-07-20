#!/usr/bin/env python3
"working with annotations"
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Method: element_length -function that
            returns the length of each item
            in @lst
    Param: lst - an iterable sequence
    """
    return [(i, len(i)) for i in lst]
