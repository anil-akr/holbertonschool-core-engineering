#!/usr/bin/env python3

def append_write(filename="", text=""):
    with open(filename, 'a', encoding="utf-8") as af:
        resultat = af.write(text)
        return(resultat)
