#!/usr/bin/python3
""" A module that contains from_json_string function """
import json


def from_json_string(my_str):
    """
        Returns an object represented by a JSON string
    """
    return json.loads(my_str)
