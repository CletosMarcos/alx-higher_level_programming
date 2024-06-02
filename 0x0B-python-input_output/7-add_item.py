#!/usr/bin/python3
""" Module that defines a script that adds all arguments to a Python list
    and then save them to a file

    must use your function save_to_json_file from 5-save_to_json_file.py
    must use your function load_from_json_file from 6-load_from_json_file.py
    The list must be saved as a JSON representation in a file named:
        add_item.json
    """


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

"""args_list = []

for arg_pos in range(1, len(sys.argv)):
    args_list.append(str(sys.argv[arg_pos]))

# writes an Object to a text file, using a JSON representation
save_to_json_file(args_list, "add_item.json")

# creates an Object from a JSON file
load_from_json_file("add_item.json")"""
try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []
items.extend(sys.argv[1:])
save_to_json_file(items, "add_item.json")
