#!/usr/bin/env python3
def print_square(size):
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        print("#" * size)


# print_square(4)
# print("")
# print_square(10)
# print("")
# print_square(0)
# print("")
# print_square(1)
# print("")
# try:
#     print_square(-1)
# except Exception as e:
#     print(e)
# print("")