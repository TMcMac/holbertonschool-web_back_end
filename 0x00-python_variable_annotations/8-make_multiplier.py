#!/usr/bin/env python3
"""Working with annotations"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Method: make_multiplier - take in a float and return a
    function that uses that float as a mulitpplier

    Parameters: multiplier is a float
    Return: a new function that uses multiplier as named
    """

    return lambda x: multiplier * x
