#!/usr/bin/python3
""" A module that contains a class Rectangle """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        A class Rectangle that inherits frm BaseGeometry
    """
    def __init__(self, width, height):
        """
            Instantiation with width and height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
            Returns the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
            returns a description
        """
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
