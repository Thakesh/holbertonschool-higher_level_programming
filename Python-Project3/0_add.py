#!/usr/bin/python3
def add(a, b):
    return a + b
from 0_add import add
if __name__ == "__main__":
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
