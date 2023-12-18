#!/usr/bin/python3
class Wrg(Exception):
    pass


class OutOfRg(Exception):
    pass


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    result = 0
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise OutOfRg
            elif not isinstance(my_list_1[i], (int, float)):
                raise Wrg
            elif not isinstance(my_list_2[i], (int, float)):
                raise Wrg
            else:
                result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except Wrg:
            print("wrong type")
            result = 0
        except OutOfRg:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return new_list
