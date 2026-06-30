#!/usr/bin/env python3
"""Display the value of the variable a imported from another module.

The value is shown only when this file is run directly, never when it is
imported (it is protected by the __main__ guard).
"""

from variable_load_5 import a


if __name__ == "__main__":
    print(a)
