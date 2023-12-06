#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    tmp = []
    for i in a_dictionary.items():
        a, b = i
        if b == value:
            tmp.append(a)
    for i in tmp:
        del a_dictionary[i]
    return a_dictionary
