#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 123:
            new = ord(str[i]) - 32
        else:
            new = ord(str[i])
        print("{:c}".format(new), end="")
    print("")
