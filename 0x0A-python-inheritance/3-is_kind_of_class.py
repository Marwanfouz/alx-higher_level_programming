#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class.
        Otherwise - False.
    """
    return (isinstance(obj, a_class))
