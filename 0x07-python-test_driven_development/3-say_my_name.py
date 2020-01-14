#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """ Function that prints My name is <first name> <last name> """
    try:
        print("My name is {:s} {:s}".format(first_name, last_name))
    except:
        if type(first_name) != str:
            raise TypeError('first_name must be a string')
        elif type(last_name) != str:
            raise TypeError('last_name must be a string')
