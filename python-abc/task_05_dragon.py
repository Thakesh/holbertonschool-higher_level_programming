#!/usr/bin/python3
"""This module defines SwimMixin, FlyMixin, and Dragon."""


class SwimMixin:
    """Mixin that provides swimming ability."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying ability."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that can swim and fly."""

    def roar(self):
        print("The dragon roars!")
