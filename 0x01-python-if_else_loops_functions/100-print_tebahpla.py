#!/usr/bin/python3

print("{}".format(''.join(
    chr(i - 32*(i % 2)) for i in reversed(range(97, 97 + 26))
)), end='')
