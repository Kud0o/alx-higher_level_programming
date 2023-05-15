#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < len(my_list) and idx > 0:
        res = my_list.copy()
        res[idx] = element
        return res
    else:
        return my_list.copy()
