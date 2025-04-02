#!/usr/bin/python3
""" Define a square class"""


class Square:
    """ representative of square class"""

    def __init__(self, size=0, position=(0, 0)):
        """ Initialise the newly created square
        where: size equates the size of the square and given a default value 0
        position is a tuple
        """
        self.size = size
        self.position = position

    """ Setter and getter for position"""
    @property
    def position(self):
        """ getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """ the setter for position"""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

        """ Getter for the private attr size"""
    @property
    def size(self):
        """property getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ method that returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """ print rep of square with # char..."""
        if self.__size == 0:
            print()
            return
        [print() for i in range(0, self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for item in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
