#!/usr/bin/python3

def print_list_integer(my_list=[]):
    print("{}".format(''.join(f"{i:d}\n" for i in my_list), end=''), end='')
