#!/usr/bin/python3
for i in range(0, 10):
    j = 0
    for j in range(0, 10):
        if i < j:
            print("{}{}".format(i, j), end=', ' if i + j != 17 else '')
print()
