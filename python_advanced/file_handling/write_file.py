#!/usr/bin/env python3
"""Module that writes a string to a UTF-8 text file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file.

    Args:
        filename (str): Name of the file.
        text (str): Text to write.

    Returns:
        int: Number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as wf:
        resultat = wf.write(text)
        return resultat
