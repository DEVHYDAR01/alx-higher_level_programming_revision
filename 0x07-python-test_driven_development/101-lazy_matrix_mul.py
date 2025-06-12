#!/usr/bin/env python3
import numpy as np
def lazy_matrix_mul(m_a, m_b):
    data1 = np.array(m_a)
    data2 = np.array(m_b)
    dot_product = np.dot(data1, data2)
    return dot_product

