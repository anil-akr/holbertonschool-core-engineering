#!/usr/bin/env python3
"""Display the result of 1 + 2 using an imported add() function.

The computation runs only when this file is run directly, never when it is
imported (it is protected by the __main__ guard).
"""

from add_0 import add


if __name__ == "__main__":
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
