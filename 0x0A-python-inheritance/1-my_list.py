#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for de built-in list class."""

    def print_sorted(self):
        """Print _list in sorted ascending order."""
        print(sorted(self))
