#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_old = list(a_dictionary.keys())
    list_old.sort()
    for i in list_old:
        print("{}: {}".format(i, a_dictionary.get(i)))
