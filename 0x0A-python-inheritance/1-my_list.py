#!/usr/bin/python3
""" A module that contains MyClass """


class MyList(list):
    """ A class that inherits frm list """

    def print_sorted(self):
        """
            A function that prints the list
            in ascending order
        """
        print(sorted(self))
