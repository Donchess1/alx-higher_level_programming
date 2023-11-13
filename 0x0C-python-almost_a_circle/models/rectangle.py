#!/usr/bin/python3
"...rectangle's model"

from models.base import Base

class Rectangle(Base):
    """this is the Rectangle class"""

    def __init__(self, width, height, x, y, id=None):
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
            id (int): unique number of rectangle"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def int_validate(self, arg, value):
        """initializes the value check condition"""
        if not isinstance(value, int):
            raise TypeError(f"{arg} must be an integer")
        if arg in ["x", "y"] and value < 0:
                raise ValueError(f"{arg} must be >= 0")
        elif arg in ["width", "height"] and value <= 0:
                raise ValueError(f"{arg} must be > 0")

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """validates the property of width"""
        self.int_validate("width", value)
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """validates the property of height"""
        self.int_validate("height", value)
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """validates the property of x"""
        self.int_validate("x", value)
        self.__x = value

     @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """validates the property of y"""
        self.int_validate("y", value)
        self.__y = value

    def area(self):
        """initializes area of rectangle"""
        return(self.width * self.height)

    def display(self):
        """displays the recangle"""
        for rows in range(self.y):
            print("")
        for h in range(self.height):
            for w in range(self.width + self.x):
                if w < self.x:
                    print(" ", end="" )
                else:
                    print("#", end="")
            print("")

    def __str__(self):
        """the rectangle string method"""
        a = "[{}] ({})".format(self.__class__.__name__, self.id)
        b = "{}"/"{}" - ("{}"/"{}").format(self.x, self.y, self.width, self.height)
        return(a + b)
    def update(self, *args):
        """updating recttangle with kwargs"""
        if args:
            attributes =["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
