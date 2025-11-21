#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square with validated size."""

    def __init__(self, size=0):
        self.size = size  # use setter for validation

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
