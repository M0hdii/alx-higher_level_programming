#!/usr/bin/python3
"""
Module name: square_module

This module defines a class named Square

Class:
    Square: defines a square

Attributes:
    Size : The size of the square

Usage:
    n_square = Square()

"""


class Square:
    """
    This is a class named square that defines size

    Attributes:
        ___size: the size of the square

    """
    def __init__(self, size=0):
        """
        Initialize a new instance of a square class

        Args:
            size (int): the size of the square

        Raises:
            TypeError: if size is not int
            ValueError: if value negative

        Returns:
            None
    """
        if not isinstance(size, int):

            raise TypeError("size must be a number")
        if size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size

    def area(self):

        """
        calculates the area of a current square

        Retunrs:
            the current square area
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        gets the size object

        Returns:
            the size object
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the size of a square
        """
        if not isinstance(value, int):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.area() == other.area()
        return NoImplemented

    def __ne__(self, other):
        if isinstance(other, Square):
            return self.area() != other.area()
        return NoImplemented

    def __lt__(self, other):
        if isinstance(other, Square):
            return self.area() < other.area()
        return NoImplemented

    def __le__(self, other):
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NoImplemented

    def __gt__(self, other):
        if isinstance(other, Square):
            return self.area() > other.area()
        return NoImplemented

    def __ge__(self, other):
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NoImplemented
