#!/usr/bin/env python3
"""Define an abstract Shape class and its concrete subclasses."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return (math.pi * radius ** 2)



    def perimeter(self):
        return (2 * math.pi * radius)
