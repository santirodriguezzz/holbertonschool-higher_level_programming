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
        return self.width

    @size.setter
    def size(self, size):
        """set size"""
        self.width = size
        self.height = size

    def __str__(self):
        """Creates a string object from a given object"""
        return f"[Square] ({self.id}) {self.x}/{self.y} -"\
            f" {self.width}"

    def update(self, *args, **kwargs):
        """Assigns a value argument to each attribute"""
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

        if "id" in kwargs:
            self.id = kwargs["id"]

        if "size" in kwargs:
            self.size = kwargs["size"]

        if "x" in kwargs:
            self.x = kwargs["x"]

        if "y" in kwargs:
            self.y = kwargs["y"]

    def to_dictionary(self):
        """that returns the dictionary representation"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
