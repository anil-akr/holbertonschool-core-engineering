#!/usr/bin/env python3
"""function must print the string in uppercase followed by a new line."""


def uppercase(str):
    for lettre in str:
        if 97 <= ord(lettre) <= 122:
            lettre = chr(ord(lettre) - 32)
        print("{}".format(lettre), end="")
    print()
