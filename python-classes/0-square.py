#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Defines a square."""

    def __init__(self, size):
        """Initialize a new Square with a private size.

        Args:
            size: The size of the square.
        """
        self.__size = size
