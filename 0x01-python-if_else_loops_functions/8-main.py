#!/usr/bin/python3

def uppercase(str):
    for i in str:
        if ord(i) >= 79 and ord(i) <= 79 + 26:
            print("{}".format(chr(ord(i) - 32), end=''), end='')
        else:
            print("{}".format(i, end=''), end='')

