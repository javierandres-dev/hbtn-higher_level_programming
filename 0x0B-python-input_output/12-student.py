#!/usr/bin/python3
class Student:
    """
        class Student that defines a student by: (based on 11-student.py)
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
        if attrs is not None:
            dic = {}
            for i, value in self.__dict__.items():
                for j in attrs:
                    if i == j:
                        dic.update({i: j})
            return dic
        else:
            return self.__dict__
