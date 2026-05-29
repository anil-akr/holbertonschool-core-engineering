#!/usr/bin/python3
"""Module that reads a UTF-8 text file and prints it."""


def read_file(filename=""):
    """Read and print the content of a UTF-8 text file."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
