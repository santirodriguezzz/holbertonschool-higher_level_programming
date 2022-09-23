#!/usr/bin/python3
"""function that adds ints"""


def add_integer(a, b=98):
    """check a and b"""
    if a is None or type(a) is not float and type(a) is not int:
        raise TypeError("a must be an integer")
    if a is None or type(b) is not float and type(b) is not int:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
