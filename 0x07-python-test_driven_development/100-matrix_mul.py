#!/usr/bin/env python3
def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    
    for row_list in m_a:
        for element in row_list:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    
    for row_list in m_b:
        for element in row_list:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")


    mat_c = []
    for row in range(len(m_a)):
        if len(m_a) == 1:
            #first column solution
            first_place = m_a[row][0] * m_b[0][0]
            second_place = m_a[row][1] * m_b[1][0]
            calc = first_place + second_place
            #second column solution
            position_1 = m_a[row][0] * m_b[0][1]
            position_2 = m_a[row][1] * m_b[1][1]
            second_calc = position_1 + position_2
            current_row_result = [calc, second_calc]
            mat_c.append(current_row_result)
        else:
            # first column solution
            first_place = m_a[row][0] * m_b[0][0]
            second_place = m_a[row][1] * m_b[1][0]
            first_total = first_place + second_place
            # second column soluton
            position_1 = m_a[row][0] * m_b[0][1]
            position_2 = m_a[row][1] * m_b[1][1]
            second_total = position_1 + position_2
            current_row_result = [first_total, second_total]
            mat_c.append(current_row_result)
    return mat_c
