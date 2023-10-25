#!/usr/bin/python3
"square module"


class Square:
    "define the class square"

    def __init__(self, size=0):
        "initiate size at 0"
        self.size = size

    @property def size(self):
        "set size of square"
        return self.__size

    @size.setter def size(self, value):
    if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        def area(self):
            "return area"
        result =self.__size * self.__size
        return result

    def my_print(self):
        "to print the square"
        for a in range (0, self.__size):
            [print("#", end = "")
                    for b in range (0, self.__size)]
            if self.__size = 0:
                print("")
