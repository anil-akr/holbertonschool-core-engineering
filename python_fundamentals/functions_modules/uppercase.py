#!/usr/bin/env python3
"""Display a string in uppercase using ASCII conversion."""


def uppercase(str):
    """Display the given string in uppercase, followed by a new line.

    Lowercase letters (a-z) are converted to uppercase using their ASCII
    code (ord/chr): 32 is subtracted from their code. All other characters
    are shown unchanged.

    Args:
        str: the string to convert to uppercase.
    """
    for lettre in str:
        if 97 <= ord(lettre) <= 122:
            lettre = chr(ord(lettre) - 32)
        print("{}".format(lettre), end="")
    print()
