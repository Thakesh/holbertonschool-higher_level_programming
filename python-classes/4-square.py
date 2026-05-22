#!/usr/bin/python3
"""Defines a square with size validation, getter, setter, and area method."""


class Square:
    """Square class with private size attribute and property control."""

    def __init__(self, size=0):
        self.size = size  # uses the setter for validation

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

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
