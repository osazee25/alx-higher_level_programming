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
        """Displays the rectangle with height and width value"""
        for i in range(self.height):
            for j in range(self.width):
                print("#", end="")
            print('\n', end ="")


    def __str__(self):
        """Overrides the usual __str__ method"""
        return("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height))
