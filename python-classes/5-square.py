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
        self.__size = size

    @property
    def size(self):
        """ get or set size square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size to a value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        calculates area of square
        """
        return self.__size ** 2

    def my_print(self):
        """prints a square with char #"""
        if self.__size == 0:
            print()
            return None
        else:
            print('\n'.join([''.join('#' * self.__size)] * self.__size))
