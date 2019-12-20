#!/usr/bin/python3
def search_replace(my_list, search, replace):
    change = lambda i: replace if i == search else i
    result = map(change, my_list)
    for i in my_list:
        return (list(result))
