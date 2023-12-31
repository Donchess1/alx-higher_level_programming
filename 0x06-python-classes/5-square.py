#!/usr/bin/python3
"square module"


class Square:
    "define the class square"

    def __init__(self, size=0):
        "initiate size. Args:size (int): size of square"
        self.size = size

    @property
    def size(self):
        "set size of square"
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        "calculate area of square"
        result = (self.__size ** 2)
        return result
    def my_print(self):
        "to print the square"
        for a in range(0, self.__size):
            [print("#", end="") for b in range(self.__size)]
        if self.__size == 0:
            print("")
