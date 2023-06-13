#!/usr/bin/python3
"""Write a function that reads a text file (UTF8) and prints it to stdout."""


def read_file(filename="", text=""):
    """Write a string to a UTF8 text file.
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
