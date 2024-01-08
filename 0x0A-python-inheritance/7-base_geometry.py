#!/usr/bin/python3
""" A module that contains BaseGeometry class """


class BaseGeometry:
    """ A class based on 6-base_geometry.py """

    def area(self):
        """
            A public instance method that raises
            an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            A method that validates Value
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
