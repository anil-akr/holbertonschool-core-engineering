#!/usr/bin/env python3
"""function must print the string in uppercase followed by a new line."""


def uppercase(str):
    resultat = ""
    for lettre in str:
        if 97 <= ord(lettre) <= 122:
            nouvelle_lettre = chr(ord(lettre) - 32)
        else:
            nouvelle_lettre = lettre

        resultat = resultat + nouvelle_lettre
    print(resultat)
