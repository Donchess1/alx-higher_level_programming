#!/usr/bin/python3
"""square module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size, x = 0, y = 0, id = None):
        self.x = x
        self.y = y
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        a = "[{}] ({})".format(self.__class__.__name__, self.id)
        b = "{}/{}-{}".format(self.x, self.y, self.width)
        return a + b
    @property
    def size(self, size):
        return size.width
    @size.setter
        if size <= 0:
            raise ValueError ("width must be an integer")
        if not isinstance (size, int):
            raise TypeError ("width must be an integer")
        self.width = size
        self.height = size
    def update(self, *args, **kwargs):
        if args:
            ter=["id", "size", "x", "y"]
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
