#!/usr/bin/python3
"""
2D Matrix rotation module
"""

def rotate_2d_matrix(matrix):
    x = 0
    n = len(matrix)
    l = n

    while l > 0:
        y = n - 1
        while y >= 0:
            val = matrix[y].pop(0)
            matrix[x].append(val)
            y -= 1

        l -= 1
        x += 1

