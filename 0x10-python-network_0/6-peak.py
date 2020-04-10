#!/usr/bin/python3
# function that finds a peak in a list of unsorted integers.


def aux(list_of_integers, first, last):
    """ recursive auxiliary function """
    x = last - first
    if x == 1:
        if list_of_integers[first] > list_of_integers[last]:
            return first
        else:
            return last
    middle = first + x // 2
    if list_of_integers[middle] < list_of_integers[middle + 1]:
        return aux(list_of_integers, middle, last)
    return aux(list_of_integers, first, middle)


def find_peak(list_of_integers):
    """ function that finds a peak in a list of unsorted integers """
    if len(list_of_integers) == 0:
        return None
    return list_of_integers[aux(
        list_of_integers, 0, len(list_of_integers) - 1)]
