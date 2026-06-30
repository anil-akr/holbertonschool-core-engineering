#!/usr/bin/env python3
"""Import add() from add_0 and display the result of 1 + 2.

The computation runs only when this file is executed directly, never when
it is imported (it is protected by the __main__ guard).
"""

from add_0 import add


if __name__ == "__main__":
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
