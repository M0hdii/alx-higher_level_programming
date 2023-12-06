#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = {}
    for i in a_dictionary.items():
        a, b = i
        new_d[a] = b * 2
    return new_d
