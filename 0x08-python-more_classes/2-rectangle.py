#!/usr/bin/python3
"""
This is a module that creates a class
which returns a perimeter and the area of
rectangle
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        calculate area of a rectangle
        """
    return self.__width * self.__heigh

    def perimeter(self):
        """
        calculate perimeter of a rectangle
        """
    return 2 * (self.__width + self.__height)
