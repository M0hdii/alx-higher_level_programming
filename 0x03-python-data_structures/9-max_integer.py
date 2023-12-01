#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    m = my_list[0]
    for i in range(len(my_list)):
        if m < my_list[i]:
            m = my_list[i]
    return m
