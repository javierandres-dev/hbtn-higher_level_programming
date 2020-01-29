#!/usr/bin/python3
""" shebang line - defines where the interpreter is located """
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
        if list_dictionaries is None or list_dictionaries == '':
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
             class method that writes the JSON string
             representation of list of instances who inherits of Base
        """
        my_list = []
        if list_objs:
            for i in list_objs:
                my_list.append(i.to_dictionary())
        r = cls.to_json_string(my_list)
        with open('{:s}.json'.format(cls.__name__),
                  mode='w', encoding='utf-8') as f:
            f.write(r)

    @staticmethod
    def from_json_string(json_string):
        """
            static method that returns the list of
            the JSON string representation
        """
        my_list = []
        if json_string is None or json_string is '':
            return my_list
        else:
            my_list = json.loads(json_string)
            return my_list

    @classmethod
    def create(cls, **dictionary):
        """
            class method that returns an instance
            with all attributes already set
        """
        if cls.__name__ == 'Rectangle':
            my_dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            my_dummy = cls(1)
        my_dummy.update(**dictionary)
        return my_dummy

    @classmethod
    def load_from_file(cls):
        """ class method that returns a list of instances """
        my_list = []
        filename = cls.__name__ + '.json'
        try:
            with open(filename, mode='r', encoding='utf-8') as f:
                r = cls.from_json_string(f.read())
                for i in r:
                    my_list.append(cls.create(**i))
        except:
            pass
        return my_list
