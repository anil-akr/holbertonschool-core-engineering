#!/usr/bin/env python3
"""Defines a Square class with controlled access to size and position."""


class Square:
    """Represents a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square instance with validation."""

        # Validate size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        # Validate position
        if (
            not isinstance(position, tuple)
            or len(position) != 2
            or not all(isinstance(x, int) and x >= 0 for x in position)
        ):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )

        # Private attributes
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation."""

        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(x, int) and x >= 0 for x in value)
        ):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )

        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using # characters."""

        # Print empty line if size is 0
        if self.__size == 0:
            print("")
            return

        # Print vertical offset
        for _ in range(self.__position[1]):
            print("")

        # Print the square with horizontal offset
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return the string representation of the square."""

        # Return empty string if size is 0
        if self.__size == 0:
            return ""

        lines = []

        # Add vertical offset
        for _ in range(self.__position[1]):
            lines.append("")

        # Add square rows
        for _ in range(self.__size):
            lines.append(
                " " * self.__position[0] + "#" * self.__size
            )

        return "\n".join(lines)
