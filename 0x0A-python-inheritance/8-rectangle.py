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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
