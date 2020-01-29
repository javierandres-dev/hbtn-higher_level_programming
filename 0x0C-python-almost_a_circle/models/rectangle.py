#!/usr/bin/python3
""" shebang line - defines where the interpreter is located """
from models.base import Base
""" import module """


class Rectangle(Base):
    """ class that inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
        """ attribute access """

    @property
    def width(self):
        """ getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter """
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter """
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        """ getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter """
        if type(value) != int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """ getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter """
        if type(value) != int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """
            public method that returns the area
            value of the Rectangle instance
        """
        return self.width * self.height

    def display(self):
        """
            method public that prints in stdout
            the Rectangle instance with the character #
        """
        for i in range(self.y):
            print('')
        for i in range(self.height):
            print(' ' * self.x, end='')
            for j in range(self.width):
                print('#', end='')
            print('')

    def __str__(self):
        """ overriding the __str__ method """
        return ('[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """
            public method that assigns a key/value argument to each attribute
        """
        list_attr = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, list_attr[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
            public method that returns the dictionary
            representation of a Rectangle
        """
        my_dict = {'id': self.id, 'width': self.width,
                   'height': self.height, 'x': self.x, 'y': self.y}
        return my_dict
