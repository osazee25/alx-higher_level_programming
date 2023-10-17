#!/usr/bin/python3

"""Base class definition"""
class Base:
    """Represent the base model.

    Represents the "base" for all other classes in project 0x0C*.

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    _nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiating the Base class
        
        Args:
            id(int): The id of class attribute
        """

        if id != None:
            self.id = id

        else:
            Base._nb_objects += 1
            self.id = Base._nb_objects
