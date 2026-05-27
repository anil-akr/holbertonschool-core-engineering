#!/usr/bin/env python3
"""Module that appends text to a file."""


def append_write(filename="", text=""):
    """Append a string at the end of a UTF-8 text file.

    Args:
        filename (str): Name of the file.
        text (str): Text to append.

    Returns:
        int: Number of characters added.
    """
    with open(filename, 'a', encoding="utf-8") as af:
        resultat = af.write(text)
        return resultat
