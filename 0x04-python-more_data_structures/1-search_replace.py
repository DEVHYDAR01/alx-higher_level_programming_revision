#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [i for i in my_list]
    for i in range(1, len(new_list) - 1):
        if i == search - 1:
            new_list[i] = replace
    return new_list