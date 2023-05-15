#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < len(my_list) or idx > 0:
        res = []
        res += my_list[0:idx]
        res += [element]
        res += my_list[idx+1:]
        return res
    else:
        return my_list.copy()
    
