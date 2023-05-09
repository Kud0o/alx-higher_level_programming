#!/usr/bin/python3

def uppercase(str):
    strl = list(str)
    c = 0
    for i in strl:
        if ord(i) >= 97 and ord(i) <= 97 + 26:
            strl[c] = chr(ord(i) - 32)
       c = c + 1
    print("{}".format(''.join(strl), end=''))
