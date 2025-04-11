#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total_count = 0
    int_convert = []
    if len(roman_string) == 1:
        if roman_string in roman_dict:
            total_count = roman_dict[roman_string]
            return total_count
    else:
        for i in roman_string:
            if i in roman_dict:
                int_convert.append(roman_dict[i])
    for integer in int_convert:
        if int_convert[0] < int_convert[1]:
            total_count = int_convert[1] - integer
            return total_count
        total_count += integer
    return total_count