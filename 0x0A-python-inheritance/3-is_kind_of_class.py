#!/usr/bin/python3
""" A module that contain is_kind_of_class function """


def is_kind_of_class(obj, a_class):
    """
        Checks of the object is an instance of,
        or if the object is an instance of a class
        that inherited from, the specified class

        Args:
            obj: The object
            a_class: The class

        Return:
            True, otherwise False
    """
    return isinstance(obj, a_class)
