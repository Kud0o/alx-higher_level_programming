#!/usr/bin/python3

def print_last_digit(number):
    d = int(abs(number) % 10 * (number / abs(number)))
    print("{}".format(d, end=''), end='')
    return d
