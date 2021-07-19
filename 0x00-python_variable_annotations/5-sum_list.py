#!/usr/bin/env python3
"""Working with annotations"""

def sum_list(input_list: list[float]) ->float:
    """
    Method: sum_list - sums a list of floats
    Parameters: input_list is a list of floats
    Return: a sum of input_list of type float
    """
    result: float = 0
    for num in input_list:
        result += num

    return (result)
