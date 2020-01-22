#!/usr/bin/python3
"""
    script that adds all arguments to a Python list,
    and then save them to a file
"""
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
import sys
try:
    pl = load_from_json_file('add_item.json')
except:
    pl = []
for i in range(1, len(sys.argv)):
    pl.append(sys.argv[i])
save_to_json_file(pl, "add_item.json")
