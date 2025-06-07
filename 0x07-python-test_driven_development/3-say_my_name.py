#!/usr/bin/env python3
def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str) and not isinstance(last_name, str):
        raise TypeError("first_name and last_name must both be a string")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))