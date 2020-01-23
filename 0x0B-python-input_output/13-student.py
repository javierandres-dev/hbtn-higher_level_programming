#!/usr/bin/python3
class Student:
    """
        class Student that defines a student by: (based on 12-student.py)
    """
    def __init__(self, first_name, last_name, age):
        """ constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            public method that retrieves a dictionary representation
            of a Student instance (same as 10-class_to_json.py)
        """
        if not isinstance(attrs, list):
            return self.__dict__
        for i in attrs:
            if not isinstance(i, str):
                return self.__dict__
        dic = {}
        for j in attrs:
            if j in self.__dict__.keys():
                dic[j] = self.__dict__[j]
        return dic

    def reload_from_json(self, json):
        """
            Public method that replaces all attributes of the Student instance
        """
        for i in json:
            self.__dict__[i] = json[i]
