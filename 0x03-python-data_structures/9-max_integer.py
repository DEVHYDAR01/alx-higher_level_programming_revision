#!/usr/bin/python
def max_integer(my_list=[]):
    if my_list == []:
        return None
    max = 0
    for i in my_list:
        if i > max:
            max = i
    return max