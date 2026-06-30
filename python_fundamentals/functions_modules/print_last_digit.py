#!/usr/bin/env python3

number = __import__('random').randint(-10000, 10000)


def print_last_digit(number):
    last_digit = abs(number) % 10

    if number < 0:
        last_digit = -last_digit

    else:
        return last_digit
