#!/usr/bin/python3
"""Define a Square Class"""


class Square:
    """what's a square and it's functionalities"""

    def __init__(self, size=0, position=(0, 0)):
        """New Square instance"""
        self.__size = size
        self.position = position

    @property
    def size(self):
        """retrieves the square's size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value, for size"""
        if not isinstance(value, int):  # checks that value's an int
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """retrieves the square's position"""
        return self.__position

    @position.setter
    def position(self, value):
        """private instance attribute"""
        if len(value) != 2 or type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """finds and retrieves square's area"""
        return self.__size ** 2

    def my_print(self):
        """prints to stdout the square with car #"""
        if self.__size == 0:
            print()
            return None
        else:
            for i in range(0, self.__position[1]):
                print()
            for j in range(0, self.__size):
                for h in range(0, self.__position[0]):
                    print(" ", end="")
                for l in range(0, self.__size):
                    print("#", end="")
                print()