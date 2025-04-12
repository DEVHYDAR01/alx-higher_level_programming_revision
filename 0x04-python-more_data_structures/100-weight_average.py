#!/usr/bin/python
def weight_average(my_list=[]):
    total_sum_of_tuple = 0
    total_sum_of_divide_by = 0
    multiply_tuple_list = [tuple[0] * tuple[1] for tuple in my_list]
    get_tuple_divide_by = [tuple[1] for tuple in my_list]
    for i in range(len(multiply_tuple_list)):
        total_sum_of_tuple += multiply_tuple_list[i]
        total_sum_of_divide_by += get_tuple_divide_by[i]
    weighted_average = total_sum_of_tuple / total_sum_of_divide_by 
    return weighted_average





my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))