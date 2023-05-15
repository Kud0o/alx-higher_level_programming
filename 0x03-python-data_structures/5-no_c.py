#!/usr/bin/python3

def no_c(my_string):
    strl = list(my_string)
    res = []
    c = 0
    for i in strl:
        if i == 'c' or i == 'C':
            continue
        else:
            res += [i]
    return ''.join(res)
