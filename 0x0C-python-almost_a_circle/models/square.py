#!/usr/bin/python3
""" shebang line - defines where the interpreter is located """
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

    def update(self, *args, **kwargs):
        """ public method that assigns attributes """
        list_attr = ['id', 'size', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, list_attr[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
            public method that returns the dictionary
            representation of a Square
        """
        my_dict = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return my_dict
