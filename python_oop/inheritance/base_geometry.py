#!/usr/bin/env python3
"""This class represents a foundational concept for geometric shapes.
It defines behavior that other shape classes will build upon"""

class BaseGeometry:
    """Base class for geometric shapes."""

    def area(self):
        """Raises an exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

