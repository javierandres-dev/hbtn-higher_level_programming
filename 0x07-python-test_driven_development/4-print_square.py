def print_square(size):
    if type(size) == int and size > 0:
        for i in range(size):
            for j in range(size):
                print('#', end='')
            print('')
    elif type(size) == float and size < 0:
        raise TypeError('size must be an integer')
    elif type(size) != int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
