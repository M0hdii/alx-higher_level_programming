#!/usr/bin/python3
""" A module that contains the read_file function """


def read_file(filename=""):
    """
        Reads a text file and prints it to stdout

        Args:
            filename: The file to read
    """
    with open(filename, encoding="utf-8") as f:
        a = f.read()

    print(a, end="")
