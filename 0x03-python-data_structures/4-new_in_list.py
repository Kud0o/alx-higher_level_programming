#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    res = list(my_list)
    if idx >= len(my_list) or idx < 0:
        return res
    else:
        res[idx] = element
        return res
