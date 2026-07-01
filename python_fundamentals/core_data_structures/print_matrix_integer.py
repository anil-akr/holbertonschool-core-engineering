#!/usr/bin/env python3
"""function that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for index in range(len(row)):
            if index == len(row) - 1:
                print("{:d}".format(row[index]), end="")
            else:
                print("{:d}".format(row[index]), end=" ")
        print()
