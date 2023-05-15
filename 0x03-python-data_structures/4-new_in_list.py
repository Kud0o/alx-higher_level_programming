#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    res = my_list.copy()
    if idx >= len(my_list) or idx < 0:
        res[idx] = element
        return res
    else:
        res[idx] = element
        return res
