#!/usr/bin/env python3
"""function that adds two tuples."""


def add_tuple(tuple_a=(), tuple_b=()):
    value_a_first = tuple_a[0] if len(tuple_a) > 0 else 0
    value_a_second = tuple_a[1] if len(tuple_a) > 1 else 0
    value_b_first = tuple_b[0] if len(tuple_b) > 0 else 0
    value_b_second = tuple_b[1] if len(tuple_b) > 1 else 0

    return (value_a_first + value_b_first, value_a_second + value_b_second)
