#!/usr/bin/python
def max_integer(my_list=[]):
    if my_list == []:
        return None
    max = 0
    for i in my_list:
        if i > max:
            max = i
    return max

# my_list = [1, 90, 2, 13, 34, 5, -13, 3]
# max_value = max_integer(my_list)
# print("Max: {}".format(max_value))