#!/usr/bin/env python3
"""function that returns the key with the biggest integer value."""


def best_score(a_dictionary):
    best_key = None

    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    for key in a_dictionary:
        if best_key is None or a_dictionary[key] > a_dictionary[best_key]:
            best_key = key
    return best_key
