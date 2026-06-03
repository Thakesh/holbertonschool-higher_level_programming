#!/usr/bin/python3
"""This module defines a MyList class."""


class MyList(list):
    """This class inherits from list."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""

        print(sorted(self))
