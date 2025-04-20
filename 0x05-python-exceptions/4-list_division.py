#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    length = []
    try:
        for i in range(list_length):
            result = my_list_1[i] / my_list_2[i]
            length.append(result)
    except (ZeroDivisionError, TypeError, IndexError):
        if ZeroDivisionError:
            print("division by 0")
        if TypeError:
            print("wrong type")
        if IndexError:
            print("out of range")
    finally:
        new_length = []
        for i in range(list_length):
            try:   
                result = my_list_1[i] / my_list_2[i]
                new_length.append(result)
            except (ZeroDivisionError, TypeError, IndexError):
                if ZeroDivisionError or TypeError or IndexError:
                    result = 0
                    new_length.append(result)
        return new_length