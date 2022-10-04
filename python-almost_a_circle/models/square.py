#!/usr/bin/python3
"""interpreter"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize square class"""
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """retrive size"""
        return self.__width

    @size.setter
    def size(self, size):
        """set size"""
        self.__width = size
        self.__height = size

    def __str__(self):
        """Creates a string object from a given object"""
        return f"[Square] ({id}) {self.__x}/{self.__y} -"\
            f" {self.__width}/{self.__height}"