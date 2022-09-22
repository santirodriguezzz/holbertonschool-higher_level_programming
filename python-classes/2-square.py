#!/usr/bin/python3
""" create empty
class square
"""


class Square:
    """
    class square
    """
    def __init__(self, size=0):
        """ init is a method for
        initialize and give to
        values for an object"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
