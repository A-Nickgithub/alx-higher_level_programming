#!/usr/bin/python3
"""
A module containig a class rectangle that inherits from
BaseGeometry
which is defined in a file in the same directory
"""


class BaseGeometry:
    """Base class representing base geometry."""

    def area(self):
        """Raises an Exception with the message
        'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value and raises exceptions if not valid."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class representing a rectangle."""

    def __init__(self, width, height):
        """Initializes a Rectangle instance with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
