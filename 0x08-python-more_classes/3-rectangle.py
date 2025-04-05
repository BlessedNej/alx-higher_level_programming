#!/usr/bin/python3
""" The rectangle class module"""


class Rectangle:
    """ The rectangle class initialization"""
    def __init__(self, width=0, height=0):
        """ Instantiation of the class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ the getter for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ the setter for the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ the getter for the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """the setter for the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """public instance method to calc area of rectangle"""
        return self.height * self.width

    def perimeter(self):
        """ public instance method to calc perimeter of rectangle"""
        if self.height == 0 or self.width == 0:
            return (0)
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """ the string rep of the object"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rec_print = []
        for i in range(self.__height):
            [rec_print.append("#") for j in range(self.width)]
            if i != self.height - 1:
                rec_print.append("\n")
        return ("".join(rec_print))
