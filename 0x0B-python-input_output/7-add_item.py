#!/usr/bin/python3

"""Add all arguments to a Python list and save them to a file."""


import sys
if __name__ == "__main__":
    from save_to_json_file import ('7-save_to_json_file').save_to_json_file
    from load_from_json_file import ('8-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
