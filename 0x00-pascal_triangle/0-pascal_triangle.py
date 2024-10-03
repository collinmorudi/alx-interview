#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    print the pascal triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]  # The first row is always [1]

    for i in range(1, n):
        row = [1]  # Start each row with 1
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle
