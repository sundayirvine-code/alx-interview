#!/usr/bin/python3
"""
2D Matrix rotation module
"""

def rotate_2d_matrix(matrix):
    rotated_matrix = []
    x = 0
    n = len(matrix)
    l = n

    while l > 0:
        new_list = []
        y = n
        while y > 0:
            new_list.append(matrix[y][x])
            y -= 1

        rotated.append(new_list)
        l -= 1
        x += 1

    return rotated_matrix

