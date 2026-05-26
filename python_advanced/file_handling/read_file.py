#!/usr/bin/env python3

def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as rf:
        fc = rf.read()
        print(fc,end="")
