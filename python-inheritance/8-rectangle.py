#!/usr/bin/python3
"""python interpreter"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """function"""

    def __init__(self, width, height):
        """initialize"""
        self.integer_validator("width",width)
        self.integer_validator("height",height)
        self.width = width
        self.height = height 
