#!/usr/bin/python3
""" Define a square class"""


class Square:
    """ representative of square class"""

    def __init__(self, size=0):
        """ Instantiation with size for our object
        initialization
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ method that returns the current square area"""
        return (self.__size * self.__size)
