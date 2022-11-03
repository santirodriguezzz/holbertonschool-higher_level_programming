#!/usr/bin/python3
"""python interpreter"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size):
        """ initialize new instance Square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area"""
        return self.__size * self.__size
