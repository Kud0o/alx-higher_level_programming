#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    res = set()
    for i in set_1:
        if not i in set_2:
            res.add(i)

    for i in set_2:
        if not i in set_1:
            res.add(i)
    return res
