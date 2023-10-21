#!/usr/bin/python3

"""Module containing the Base class"""
from models.base import Base

"""Class rectangle that inherits from Base class"""

class Rectangle(Base):
    """Class rectangle that inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new rectangle

        Args:
            width(int): width of new rectangle
            height(int): height of new rectangle
            x(int): x coordinate of new rectangle
            y(int): y coordinate of new rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get/set value for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value


    @property
    def height(self):
        """get/set value for the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value


    @property
    def x(self):
        """get/set value for the x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value


    @property
    def y(self):
        """get/set value for the y coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
    
    def area(self):
        """Returns the area of the rectangle"""
        return self.height * self.width

    def display(self):
        """
    Display the rectangle with '#' characters, accounting for x and y coordinates.

    This method prints the rectangle with dimensions determined by its
    height and width attributes, and it takes care of the x and y coordinates.

    Returns:
        None
    """
        for y in range(self.y):
            print()
        for i in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()


    def __str__(self):
        """Overrides the usual __str__ method"""
        return("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
    """
    Update the attributes of the Rectangle
    This method allows you to update the attributes of the Rectangle
    using either positional arguments (*args) or keyword arguments (**kwargs).

    Args:
        *args: Positional arguments in the order (id, width, height, x, y).
        **kwargs: Keyword arguments with attribute names as keys.

    Returns:
        None
    """
    if args:
        attributes = ["id", "width", "height", "x", "y"]
        for i, arg in enumerate(args):
            if arg is not None:
                setattr(self, attributes[i], arg)

    if kwargs:
        for key, value in kwargs.items():
            if key in ("id", "width", "height", "x", "y") and value is not None:
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""

        obj_dictionary = {'id': self.id, 'width': self.__width,
                          'height': self.__height, 'x': self.__x,
                          'y': self.__y}

        return obj_dictionary

