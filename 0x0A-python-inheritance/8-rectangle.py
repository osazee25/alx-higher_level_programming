#!/usr/bin/python3
"""defines a class rectangle that inherits
from baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class that defines a rectangle using
    BaseGeometry"""

    def __init__(self, width, height):
        """Intializes a new Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
