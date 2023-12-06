#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    res = 0
    new = list(new_list)
    for i in range(len(new)):
        res += new[i]
    return res
