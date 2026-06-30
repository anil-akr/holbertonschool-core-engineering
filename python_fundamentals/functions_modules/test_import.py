#!/usr/bin/env python3
"""Import simple_add to observe that importing prints nothing.

Thanks to the if __name__ == "__main__" guard in simple_add, importing
the module only defines add(); the top-level print does not run here.
"""

import simple_add
