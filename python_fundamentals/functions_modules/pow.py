#!/usr/bin/env python3
"""Compute a raised to the power of b without the exponent operator."""


def pow(a, b):
    result = 1
    for _ in range(abs(b)):
        result *= a
    if b < 0:
        result = 1 / result
    return result
