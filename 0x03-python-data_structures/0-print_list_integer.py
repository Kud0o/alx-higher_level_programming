#!/usr/bin/python3

def print_list_integer(my_list=[]):
    if len(my_list) > 0:
        print("{}".format(''.join(f"{i}\n" for i in my_list), end=''), end='')
