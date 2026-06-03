#!/usr/bin/python3
"""This module defines VerboseList."""


class VerboseList(list):
    """A list that prints notifications on modifications."""

    def append(self, item):
        """Add item to list and print notification."""
        super().append(item)
        print("Added {} to the list.".format(item))

    def extend(self, iterable):
        """Extend list and print number of items added."""
        count = len(iterable)
        super().extend(iterable)
        print("Extended the list with {} items.".format(count))

    def remove(self, item):
        """Remove item from list and print notification."""
        print("Removed {} from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop item from list and print notification."""
        item = self[index]
        print("Popped {} from the list.".format(item))
        return super().pop(index)
