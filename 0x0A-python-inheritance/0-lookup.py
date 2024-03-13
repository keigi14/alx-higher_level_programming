#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Return a listof an object_s available attributes."""
    return (dir(obj))
