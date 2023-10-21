#!/usr/bin/python3
""" this module contains a square class"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Represents a square that inherits from class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

        def __str__(self):
        """Defines a format for the string representation of the class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """Gets the value of size"""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets the value for size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
    """
    Update the attributes of the Square.

    This method allows you to update the attributes of the Square
    using either positional arguments (*args) or keyword arguments (**kwargs).

    Args:
        *args: Positional arguments in the order (id, size, x, y).
        **kwargs: Keyword arguments with attribute names as keys.

    Raises:
        TypeError: If 'id' is not an integer (if provided).

    Returns:
        None
    """
    if args:
        attributes = ["id", "size", "x", "y"]
        for i, arg in enumerate(args):
            if arg is not None:
                if i == 0:
                    if not isinstance(arg, int):
                        raise TypeError("id must be an integer")
                setattr(self, attributes[i], arg)
    
    if kwargs:
        for key, value in kwargs.items():
            if key in ("id", "size", "x", "y") and value is not None:
                if key == "id" and not isinstance(value, int):
                    raise TypeError("id must be an integer")
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""

        obj_dictionary = {'id': self.id, 'size': self.size, 'x': self.x,
                          'y': self.y}

        return obj_dictionary
