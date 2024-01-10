#!/usr/bin/python3
""" A module that contains save_to_json_file function """
import json


def save_to_json_file(my_obj, filename):
    """
        Write an object to a text file

        Args:
            my_obj: The object to write
            filename: The text file
    """
#   a = json.dumps(my_obj)
    with open(filename, 'w', encoding="utf-8") as f:
        #       r = f.write(a)
        json.dump(my_obj, f)
