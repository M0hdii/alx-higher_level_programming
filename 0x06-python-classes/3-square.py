#!/usr/bin/python3
"""
    This module is for a class that defines a square
    based on 2-square.py
"""


class Square:
    """
        A class where we'll learn to implement
        the area of a square
    """
    def __init__(self, size=0):
        """
            Intantiation of size
        """
        if type(size) is not int:
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = size

    def area(self):
        """
            A method for the the area of the square

            Return:
                the current square of the are
        """
        return self.__size ** 2
