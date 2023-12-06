#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    first = 0
    second = 0
    for i in my_list:
        a, b = i
        first += a * b
        second += b
    return first / second
