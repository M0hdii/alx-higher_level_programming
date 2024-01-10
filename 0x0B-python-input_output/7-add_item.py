#!/usr/bin/python3
""" A script that adds all arguments to a Python list """
import sys
import json
import os
save_js = __import__('5-save_to_json_file').save_to_json_file
load_js = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    args = sys.argv

    if os.path.exists("add_item.json"):
        my_list = load_js("add_item.json")
    else:
        with open("add_item.json", 'w', encoding="utf-8") as f:
            f.write("[]")
        my_list = load_js("add_item.json")

    for i in args:
        if i == sys.argv[0]:
            continue
        else:
            my_list.append(i)

    save_js(my_list, "add_item.json")
