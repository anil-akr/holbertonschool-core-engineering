#!/usr/bin/env python3
"""Defines a Square class with controlled access to size."""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size=0):
        """Initialize a Square instance with validation."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        # Private attribute to store the size of the square
        self.__size = size

    def area(self):
        """Return the area of the square."""
        # Area = size × size
        return self.__size * self.__size

    @property
    def size(self):
        """Retrieve the size of the square."""
        # Getter: returns the private attribute
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        # Update the private attribute
        self.__size = value
