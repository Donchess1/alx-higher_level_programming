#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("enter int size")
        elif size<0:
            raise TypeError("enter a value >= zero")
        self.__size = size
