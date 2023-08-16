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
        y = n - 1
        while y >= 0:
            new_list.append(matrix[y][x])
            y -= 1

        rotated_matrix.append(new_list)
        print(new_list)
        l -= 1
        x += 1
    print(rotated_matrix)
    return rotated_matrix

