#!/usr/bin/python3
def safe_print_integer(value):
    c = 0
    try:
        print("{:d}".format(value))
    except Exception:
        return False
    else:
        return True
