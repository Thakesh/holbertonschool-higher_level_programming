#!/usr/bin/python3
"""This module defines BaseGeometry."""


class BaseGeometry:
    """Base geometry class."""

    def area(self):
        """Raise an exception because area is not implemented."""
        raise Exception("area() is not implemented")
