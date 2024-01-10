#!/usr/bin/python3
""" A module that contains the class Student """


class Student:
    """ A class that defines a student """

    def __init__(self, first_name, last_name, age):
        """ Instantiation with first_name, last_name and age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrives a dictionary representation of a Student """
        return self.__dict__
