#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_sorted = sorted(a_dictionary)
    for i in dict_sorted:
        print("{}: {}".format(i, a_dictionary[i]))