#!/usr/bin/env python3
"""Defines a Square class with its own string representation."""

Square = __import__('1-square').Square


class Square(Square):
    """Represent a square with a custom string representation."""
    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
