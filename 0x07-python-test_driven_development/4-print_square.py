#!/usr/bin/python3
def print_square(size):
    """ Function that prints a square with the character # """
    if type(size) == int and size >= 0:
        for i in range(size):
            for j in range(size):
                print('#', end='')
            print('')
    elif type(size) != int:
        raise TypeError('size must be an integer')
    else:
        raise ValueError('size must be >= 0')
