#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    comp = -90000
    comp_a = ""
    for a, b in a_dictionary.items():
        if comp < b:
            comp = b
            comp_a = a
    return comp_a
