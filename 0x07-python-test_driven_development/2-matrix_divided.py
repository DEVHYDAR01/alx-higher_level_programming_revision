def matrix_divided(matrix, div):
    row_size = 0
    if not isinstance(matrix, (int, float)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in range(len(matrix)):
        row_size = len(matrix[i])
        if row_size != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
# print(matrix_divided(matrix, 3))
print(matrix)




