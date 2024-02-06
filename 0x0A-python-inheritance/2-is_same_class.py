#!/usr/bin/python3
"""Defines class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj (any): de object to check.
        a_class (type): The class to match de type of obj to.
    Returns:
        If objext is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
