#!/usr/bin/python3
"""
Module that represents a Pascal's triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    -> Returns an empty list if n <= 0
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if i == 0 or j == 0 or i == j:
                row.append(1)
            else:
                sumDiagonals = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(sumDiagonals)
        triangle.append(row)

    return triangle
