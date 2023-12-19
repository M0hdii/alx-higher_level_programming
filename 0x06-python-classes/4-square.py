#!/usr/bin/python3
"""
    This module is for the implementation of
    getter and setter
"""


class Square:
    """
        a class Square that defines a square by: (based on 3-square.py)
    """
    def __init__(self, size=0):
        """
            instantiation
        """
        self.__size = size

    @property
    def size(self):
        """
            getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
            setter
        """
        if type(value) is not int:
            print("size must be an integer", end="")
            raise TypeError
        elif self.__size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = value

    def area(self):
        """
            Area of the square
        """
        return self.__size ** 2
