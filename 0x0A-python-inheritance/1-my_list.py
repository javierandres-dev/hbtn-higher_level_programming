#!/usr/bin/python3
class MyList(list):
    """
        A class MyList that inherits from list.  Public instance
        method that prints the list, but sorted (ascending sort)
    """
    def print_sorted(self):
        print(sorted(self))
