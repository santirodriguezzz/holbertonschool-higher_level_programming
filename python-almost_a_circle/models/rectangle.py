#!/usr/bin/python3
"""interpreter"""


from models.base import Base


class Rectangle(Base):
    """class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize class"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.errors(width, "width")
        self.errors(height, "height")
        self.errors(x, "x")
        self.errors(y, "y")

    @property
    def width(self):
        """retrive width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        self.errors(value, "width")
        self.__width = value

    @property
    def height(self):
        """retrive height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        self.errors(value, "height")
        self.__height = value
        return self.__height

    @property
    def x(self):
        """retrive x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x"""
        self.errors(value, "x")
        self.__x = value

    @property
    def y(self):
        """retrive y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        self.__y = value
        self.errors(value, "y")

    def errors(self, value, name):
        """function for errors"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0 and name in ("width", "height"):
            raise ValueError(f"{name} must be > 0")
        if value < 0 and name in ("x", "y"):
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        """return area"""
        return self.__width * self.__height

    def display(self):
        """
        It prints a rectangle of width `width` and 
        height `height` at position `x`, `y`"""
        for i in range(self.y):
            print()
        for j in range(self.height):
            for h in range(self.x):
                print(" ", end="")
            for l in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Creates a string object from a given object"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -"\
            f" {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        If there are arguments,
        then update the attributes of the class with the arguments
        """

        try:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
        except IndexError:
            pass

        if "id" in kwargs:
            self.id = kwargs["id"]

        if "width" in kwargs:
            self.width = kwargs["width"]

        if "height" in kwargs:
            self.height = kwargs["height"]

        if "x" in kwargs:
            self.x = kwargs["x"]

        if "y" in kwargs:
            self.y = kwargs["y"]

    def to_dictionary(self):
        """that returns the dictionary representation"""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
