#!/usr/bin/env python3
"""Defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a Square instance with size validation."""
        # Check that size is an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        # Check that size is not negative
        if size < 0:
            raise ValueError("size must be >= 0")

        # Private attribute to store the size
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value