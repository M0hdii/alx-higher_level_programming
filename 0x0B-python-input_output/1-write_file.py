#!/usr/bin/python3
""" This a module that contains write_file function """


def write_file(filename="", text=""):
    """
        Write a string to a text file

        Args:
            filename: The text file
            text: The string to write

        Return: The number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        a = f.write(text)
        return a
