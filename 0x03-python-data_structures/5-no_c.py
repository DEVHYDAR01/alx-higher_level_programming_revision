#!/usr/bin/python3
def no_c(my_string):
    new_string = [i for i in my_string]
    if 'c' in new_string:
        new_string.remove('c')
    if 'C' in new_string:
        new_string.remove('C')
    return ''.join(new_string)