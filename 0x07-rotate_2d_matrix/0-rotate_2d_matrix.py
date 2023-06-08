#!/usr/bin/python3
""" Module that rotates a 2D matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """ Rotates the given matrix 90 degrees clockwise
    """
    m = list(zip(*matrix[::-1]))
    for i in range(len(m)):
        for j in range(len(m[0])):
            matrix[i][j] = m[i][j]
