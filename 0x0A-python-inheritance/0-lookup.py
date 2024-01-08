#!/usr/bin/python3
""" A module for the function 'lookup' """


def lookup(obj):
    """
        A function that detects the available attributes
        and methods of an object

        Args:
            obj: The object

        Returns:
            list of available attributes and methods of
            said object
    """
    return dir(obj)
