#!/usr/bin/python3
"""
my empty class Rectangle
"""


class Rectangle:
    """
    class Rectangle
    """
    def __init__(self, width=0, height=0):
           """
        Initialize a new Rectangle object with the given width and height.

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
        """
        #self.__width = width
        #self.__height = height
    
    @property
    def width(self):
        """
        Get the width of the Rectangle.

        Returns:
            int: The width of the Rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the Rectangle.

        Args:
            value (int): The new width value for the Rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the Rectangle.

        Returns:
            int: The height of the Rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the Rectangle.

        Args:
            value (int): The new height value for the Rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value