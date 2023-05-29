#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        print("Inside result: {:0.1f}".format(a / b), end='')
        return a / b
    except Exception:
        print("Inside result: {}".format(None), end='')
        return None
    finally:
        print()
