#!/usr/bin/python3
"""interpreter"""


from models.base import Base


class Rectangle(Base):
    """class Rectangle"""
    

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    
