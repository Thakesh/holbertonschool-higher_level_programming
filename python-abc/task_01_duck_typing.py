#!/usr/bin/python3
"""This module defines Shape, Circle, Rectangle, and shape_info."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Circle shape implementation."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        r = abs(self.radius)
        return math.pi * (r ** 2)

    def perimeter(self):
        r = abs(self.radius)
        return 2 * math.pi * r


class Rectangle(Shape):
    """Rectangle shape implementation."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter of any shape (duck typing)."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
