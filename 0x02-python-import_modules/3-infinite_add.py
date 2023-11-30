#!/usr/bin/python3
import sys
if __name__ == "__main__":
    add = 0
    for i in range(len(sys.argv)):
        if i == 0:
            continue
        else:
            add += int(sys.argv[i])
    print("{:d}".format(add))
