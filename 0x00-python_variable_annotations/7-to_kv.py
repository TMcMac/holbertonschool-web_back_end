#!/usr/bin/env python3
"""Working with annotations"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Method: to_kv - make a tuple out of str and int or float squared
    Parameters: k is a string, v is int or float
    Return: tuple with k and v^2
    """

    myTuple = (k, float(v ** 2))
    return (myTuple)
