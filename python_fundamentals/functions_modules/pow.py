#!/usr/bin/env python3
"""Compute a raised to the power of b without the ** operator."""


def pow(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result
