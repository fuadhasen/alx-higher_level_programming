#!/usr/bin/python3
"""This module provide function that Create object from a JSON file. """
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
ls = load_from_json_file(filename)
if ls == None:
    ls = []
for i in range(1, len(sys.argv)):
    ls.append(sys.argv[i])

save_to_json_file(ls, filename)
