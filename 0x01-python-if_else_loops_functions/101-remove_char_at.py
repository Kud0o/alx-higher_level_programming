#!/usr/bin/python3

def remove_char_at(str, n):
    if n < 0 or n > len(str) - 1:
        print("{}".format(str, end=''))
        return "{}".format(str, end='')
    else:
        print("{}".format(''.join(str[i] for i in len(str) if i != n), end=''))
        return "{}".format(''.join(str[i] for i in len(str) if i != n), end='')
