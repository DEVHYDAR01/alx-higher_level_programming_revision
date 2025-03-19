#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx > len(my_list):
        return my_list
    new_list = [i for i in my_list]
    new_list[idx] = element
    return new_list

# new_list = [for i in range(len(my_list)) if i == idx]
            