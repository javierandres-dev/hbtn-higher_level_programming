#!/usr/bin/python3
class Student:
    """ class Student that defines a student by
        Public instance attributes: first_name, last_name, age
    """
    def __init__(self, first_name, last_name, age):
        """ constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ public method """
        return self.__dict__
