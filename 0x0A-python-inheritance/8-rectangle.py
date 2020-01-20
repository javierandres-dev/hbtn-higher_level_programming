#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ sub class Rectangle that inherits from BaseGeometry
        (based on 7-base_geometry.py).
        width and height must be private. No getter or setter
        must be positive integers, validated by integer_validator
    """
    def __init__(self, width, height):
        """ constructor """
        self.__width = width
        self.__height = height
        self.integer_validator('width', width)
        self.integer_validator('height', height)
