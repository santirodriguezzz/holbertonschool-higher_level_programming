#!/usr/bin/python3
"""python interpreter"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """function"""

    def __init__(self, width, height):
        """initialize"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self,):
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """area"""
        return self.__width * self.__height
