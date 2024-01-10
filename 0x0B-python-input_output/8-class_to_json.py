#!/usr/bin/python3
""" A module that contains the function class_to_json """


def class_to_json(obj):
    """
        Returns the dictionary description
    """
    return obj.__dict__
