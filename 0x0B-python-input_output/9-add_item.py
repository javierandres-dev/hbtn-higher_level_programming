#!/usr/bin/python3
from sys import argv
"""
    script that adds all arguments to a Python list,
    and then save them to a file
"""
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
my_list = []
try:
    my_load = load_from_json_file('add_item.json')
    for i in my_load:
        my_list.append(i)
except:
    my_list = []
for j in range(1, len(argv)):
    my_list.append(argv[j])
save_to_json_file(my_list, 'add_item.json')
