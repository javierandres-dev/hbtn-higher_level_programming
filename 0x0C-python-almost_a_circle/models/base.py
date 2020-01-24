#!/usr/bin/python3
import json
""" import module """


class Base:
    """
        First class.  This class will be the “base” of all other classes in
        this project. The goal of it is to manage id attribute in all your
        future classes and to avoid duplicating the same code
        (by extension, same bugs)
    """
    __nb_objects = 0
    """ private class attribute """

    def __init__(self, id=None):
        """ class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            static method that returns the JSON
            string representation of list of dictionaries
        """
        my_list = []
        if list_dictionaries is None or list_dictionaries == '':
            return my_list
        else:
            my_list = json.dumps(list_dictionaries)
            return my_list
