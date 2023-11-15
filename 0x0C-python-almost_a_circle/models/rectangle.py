#!/usr/bin/python3
"...rectangle's model"

from models.base import Base
class Rectangle(Base):
    """this is the Rectangle class"""

    def __init__(self, width, height, x, y):
        """Initiate the Rectangle.
        Args:
            width (int): This is the rectangle's width
            height (int): This is the rectangle's width
            x (int): coordinate x
            y (int): coordinate y
            id (int): unique number of rectangle
        Attributes:
            __width (int): This is the rectangle's width
            __height (int): This is the rectangle's width
            __x (int): coordinate x
            __y (int): coordinate y
            """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """validates the property of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """validates the property of height"""
         if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """validates the property of x"""
         if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if width < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """validates the property of y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if width < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """initializes area of rectangle"""
        return self.width * self.height

    def display(self):
        """displays the recangle"""
        for _ in range(self.y):
            print("")
        for _ in range(self.height):
            for _ in range(self.width + self.x):
                if _ < self.x:
                    print(" ", end="")
                else:
                    print("#", end="")
            print("")

    def __str__(self):
        """the rectangle string method"""
        a = "[{}] ({})".format(self.__class__.__name__, self.id)
        b = "{}"/"{}" - ("{}"/"{}").format(self.x, self.y, self.width, self.height)
        return a + b
    def update(self, *args):
        """updating recttangle with kwargs"""
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
