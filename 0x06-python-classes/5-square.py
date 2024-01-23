#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Representin a square."""

    def __init__(self, size):
        """Initialize on new square.

        Args:
            size (int): de size of de new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of de square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return de current area of de square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print de square with de # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
