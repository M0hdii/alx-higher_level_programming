#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_d = sorted(a_dictionary.items())
    for i in new_d:
        a, b = i
        print(f"{a}: {b}")
