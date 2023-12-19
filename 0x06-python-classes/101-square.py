#!/usr/bin/python3
"""
    Coordinates of a square
"""


class Square:
    """
         a class Square that defines a square by: (based on 5-square.py)
    """
    def __init__(self, size=0, position=(0, 0)):
        """
            Instantiation with optional size and optional position
        """
        if type(position) is not tuple or len(position) != 2 or not\
                all(isinstance(i, int) and i >= 0 for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(size) is not int:
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = size
            self.__position = position

    @property
    def size(self):
        """
            getter size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
            setter size
        """
        if type(value) is not int:
            print("size must be an integer", end="")
            raise TypeError
        elif value < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = value

    @property
    def position(self):
        """
            getter position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
            getter position
        """
        if type(value) is not tuple or len(value) != 2 or not\
                all(isinstance(i, int) and i > 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
            The current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
            Prints the square
        """
        if self.__size == 0:
            print()
        else:
            for L in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    def __str__(self):
        """
            same as my_print
        """
        size = self.__size
        position = self.__position
        result = ""
        if size != 0:
            [print("") for i in range(position[1])]
        for i in range(size):
            [print(" ", end="") for j in range(0, position[0])]
            [print("#", end="") for k in range(0, size)]
            if i != size - 1:
                print("")
        return ("")
