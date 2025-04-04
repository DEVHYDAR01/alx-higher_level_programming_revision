#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [i for i in my_list]
    for i in range(1, len(new_list) - 1):
        if i == search - 1:
            new_list[i] = replace
    return new_list




my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)