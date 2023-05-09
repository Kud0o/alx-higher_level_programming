#!/usr/bin/python3

def remove_char_at(str, n):
    if n < 0 or n > len(str) - 1:
        return "{}".format(str, end='')
    else:
        return "{}".format(''.join(str[i] for i in range(len(str)) if i != n), end='')
