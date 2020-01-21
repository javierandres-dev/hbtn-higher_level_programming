#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        class Square that inherits from Rectangle (9-rectangle.py).
        (task based on 10-square.py).
    """
    def __init__(self, size):
        """ constructor """
        self.__size = size
        self.integer_validator('size', size)
        super().__init__(size, size)

    def area(self):
        """ method """
        return super().area()

    def __str__(self):
        """ method """
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
