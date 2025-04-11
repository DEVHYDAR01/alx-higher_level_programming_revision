#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_score = 0
    bst_key = ''
    for key in a_dictionary:
        if a_dictionary[key] > best_score:
            best_score = a_dictionary[key]
            bst_key = key
    return bst_key

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_score(a_dictionary)
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))

# list = [2, 5, 3, 10, 20, 6, 70, 8]
# highest_val = 0
# for i in list:
#     if i > highest_val:
#         highest_val = i
# print(highest_val)