#!/bin/usr/python3
class Square:
    def __init__(self, size = 0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        return(self.__size * self.__size)
    @property
    def size(self):
        return(self.__size)
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range (0, self.__size):
                print("#" * self.__size)
