#!/usr/bin/env python3
"""Module that reads a UTF-8 text file and prints it."""


def read_file(filename=""):
    """Read and print the content of a UTF-8 text file.

    Args:
        filename (str): Name of the file to read.
    """
    with open(filename, 'r', encoding='utf-8') as rf:
        fc = rf.read()
        print(fc, end="")