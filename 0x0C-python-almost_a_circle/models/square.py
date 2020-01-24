#!/usr/bin/python3
from models.rectangle import Rectangle
""" import module """


class Square(Rectangle):
    """ class that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ constructor """
        super().__init__(size, size, x, y, id)
        """ attribute access """

    @property
    def size(self):
        """ getter """
        return self.width

    @size.setter
    def size(self, value):
        """ setter """
        self.width = value
        self.height = value

    def __str__(self):
        """ overriding the __str__ method """
        return ('[Square] ({:d}) {:d}/{:d} - {:d}'
                .format(self.id, self.x, self.y, self.size))
