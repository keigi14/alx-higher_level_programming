#!/usr/bin/python3

"""Define class Square."""


class Square:
    """Representin square."""

    def __init__(self, size=0):
        """Initialize de new square.

        Args:
            size (int): de size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return de current area of de square."""
        return (self.__size * self.__size)
