#!/usr/bin/python3
def best_score(a_dictionary):
    s = 0
    b = None
    if a_dictionary:
        b = list(a_dictionary.keys())[0]
        s = a_dictionary[b]
        for k, v in a_dictionary.items():
            if v > s:
                s = v
                b = k

    return b
