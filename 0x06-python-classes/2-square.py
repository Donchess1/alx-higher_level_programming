#!/usr/bin/python3
"Square module"
class Square:
    "square class"
    def __init__(self, size=0):
        "constructor initialing size to 0. Args:size (int): The size of the square"
        if not isinstance(size, int):
            raise TypeError("enter int size")
        elif size<0:
            raise TypeError("enter a value >= zero")
        self.__size = size
