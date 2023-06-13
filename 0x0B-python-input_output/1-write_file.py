#!/usr/bin/python3
"""Write a function that reads a text file (UTF8) and prints it to stdout."""


def read_file(filename=""):
    """Write the contents of a UTF8 text file to a text file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
