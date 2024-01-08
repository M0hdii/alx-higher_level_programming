#!/usr/bin/python3
""" A module that contains a is_same_class function """


def is_same_class(obj, a_class):
    """
        Checks if the object is an instance of a specified
        class

        Args:
            obj: The object to check
            a_class: The related class

        Returns:
            True: if the object is an instance
            False: if not
    """
    if type(obj) is a_class:
        return True
    else:
        return False
