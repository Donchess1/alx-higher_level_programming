#!/usr/bin/python3
"""square module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        a = "[{}] ({})".format(self.__class__.__name__, self.id)
        b = "{}/{}-{}".format(self.x, self.y, self.width)
        return a + b
    @property
    def size(self):
        """defines the size parameter"""
        return self.width
    @size.setter
    def size(self, value):
        """defines the size parameter"""
        self.width = value
        self.height = value
    def update(self, *args, **kwargs):
        if args:
            ter = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, ter[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
    def to_dictionary(self):
        """returns dictionary representation
        of a square"""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
