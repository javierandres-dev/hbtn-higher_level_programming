#!/usr/bin/python3
def no_c(my_string):
    char = ""
    for i in range(0, len(my_string)):
        if my_string[i] != 'C' and my_string[i] != 'c':
            char += my_string[i]
    return (char)
