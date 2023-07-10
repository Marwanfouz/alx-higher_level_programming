#!/usr/bin/python3
"""Define an Inherted list class MYList."""


class MyList(list):
    """Implemented sorting printing from the bulit-in list class."""
    def print_sorted(self):
        """that prints the list, but sorted (ascending sort)."""
        print(sorted(self))
