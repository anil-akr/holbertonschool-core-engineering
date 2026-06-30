#!/usr/bin/env python3
"""Display the four basic operations on a = 10 and b = 5.

The functions are imported from a separate module, and the operations are
shown only when this file is run directly (never when it is imported).
"""

from calculator_1 import add, sub, mul, div


if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
