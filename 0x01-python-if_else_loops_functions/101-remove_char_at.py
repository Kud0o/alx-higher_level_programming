#!/usr/bin/python3

def remove_char_at(str, n):
    if n < 0:
        print("{}".format(str, end=''))
    else:
        strl = list(str)
        del strl[n]
    print("{}".format(''.join(strl), end=''))
