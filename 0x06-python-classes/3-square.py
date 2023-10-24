#!/usr/bin/python3
"Square module"
class Square:
    "Square class defined"
    def __init__(self, size=0):
        "initialing size to 0"
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        result =self.__size * self.__size
        "return value of area"
        return result
