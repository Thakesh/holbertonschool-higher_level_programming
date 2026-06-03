#!/usr/bin/python3
"""This module defines CountedIterator."""


class CountedIterator:
    """Iterator that counts how many items have been iterated over."""

    def __init__(self, iterable):
        """Initialize with an iterator and a counter."""
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return the iterator itself."""
        return self

    def __next__(self):
        """Return next item and increment counter."""
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return number of items iterated so far."""
        return self.count
