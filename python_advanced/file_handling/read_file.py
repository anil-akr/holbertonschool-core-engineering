#!/usr/bin/python3
"""Read a file and print it."""


def read_file(filename=""):
    """Print the contents of a UTF-8 text file."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
