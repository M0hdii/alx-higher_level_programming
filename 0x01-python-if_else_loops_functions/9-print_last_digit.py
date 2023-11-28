#!/usr/bin/python3
def print_last_digit(number):
    last_n = abs(number) % 10
    print(last_n, end="")
    return last_n
