#!/usr/bin/python3
"""
    This module is an implementation of
    printing a square
"""


class Square:
    """
        a class Square that defines a square by: (based on 4-square.py)
    """
    def __init__(self, size=0):
        """
            Instantiation with optional size
        """
        self.__size = size

    @property
    def size(self):
        """
            getter
        """
        return size.__size

    @size.setter
    def size(self, value):
        """
            setter
        """
        if type(value) is not int:
            print("size must be an integer", end="")
            raise TypeError
        elif value < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = value

    def area(self):
        """
            The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
            prints the square with #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
