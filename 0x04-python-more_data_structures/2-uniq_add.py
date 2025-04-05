#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    new_set = {i for i in my_list}
    for i in new_set:
        total += i
    return total