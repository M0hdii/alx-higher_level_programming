#!/usr/bin/python3
""" A module that contains inherits_frm function """


def inherits_from(obj, a_class):
    """
        Checks if the object is an instance of a class
        that inherited directly or indirectly from
        the specified class

        Args:
            obj: The object
            a_class: The specified class

        Returns:
            True if yes, False otherwise
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
