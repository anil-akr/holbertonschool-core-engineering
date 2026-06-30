#!/usr/bin/env python3
"""Display the last digit of a number using its absolute value."""


def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
