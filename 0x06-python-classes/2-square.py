#!/usr/bin/python3
"""
    This module contains a class that defines
    a square by:(based on 1-square.py)
"""


class Square:
    """
        This is a class of where we'll learn
        size validation
    """

    def __init__(self, size=0):
        """
            initialisation of size
            args:
                size: the size of the square
        """
        if type(size) is not int:
            print("size must be an integer", end="")
            raise IndexError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = size
