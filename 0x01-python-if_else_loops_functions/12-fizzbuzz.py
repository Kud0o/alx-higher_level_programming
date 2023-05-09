#!/usr/bin/python3

def fizzbuzz():
    for i in range(101):
        if i % 3 == 0:
            print("{d}".format(d="Fizz", end=''), end='')
        if i % 5 == 0:
            print("{d}".format(d="Buzz", end=''), end='')
        if i % 3 != 0 and i % 5 != 0:
            print("{d}".format(d=i, end=''), end='')
        print(" ", end='')
    print('')
