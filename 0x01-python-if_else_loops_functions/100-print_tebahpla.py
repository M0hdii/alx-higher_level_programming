#!/usr/bin/python3
def uppercase(s):
    if s >= 97 and s <= 123:
        new = s - 32
        return new
    else:
        new = s
        return new


alpha = 122
while alpha > 96:
    if (alpha % 2) != 0:
        print("{:c}".format(uppercase(alpha)), end="")
    else:
        print("{:c}".format(alpha), end="")
    alpha -= 1
