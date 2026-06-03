#!/usr/bin/python3
"""This module defines inherits_from."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
