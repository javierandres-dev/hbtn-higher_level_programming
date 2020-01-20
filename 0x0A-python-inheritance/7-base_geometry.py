#!/usr/bin/python3
class BaseGeometry:
    """ class BaseGeometry (based on 6-base_geometry.py). """
    def area(self):
        """ Public instance method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Public instance method """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
