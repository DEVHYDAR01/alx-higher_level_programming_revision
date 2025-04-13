#!/usr/bin/python
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            try:
                print(my_list[i], end="")
                count += 1
            except IndexError:
                print("\n[DEBUG] IndexError caught at index:", i)
                break
    finally:
        print()
    return count



my_list = [1, 2, 3, 4, 5]
nb_print = safe_print_list(my_list, 2)
# print(nb_print)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))





    # list_len = 0
    # for i in my_list:
    #     list_len += 1
    # counter = 0
    # new_list = [print("{}\n".format(my_list[i]), end="") for i in range(list_len) if not my_list[i] >= x+1]
    # for nb in new_list:
    #     counter += 1
    # return counter