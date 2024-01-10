#!/usr/bin/python3
""" A module that contains the append_write function """


def append_write(filename="", text=""):
    """
        Appends a string at the end of a text file

        Args:
            filename: The file to append to
            text: The string to append

        Returns:
            The number of characters added
    """

    with open(filename, 'a', encoding="utf-8") as f:
        a = f.write(text)
        return a

