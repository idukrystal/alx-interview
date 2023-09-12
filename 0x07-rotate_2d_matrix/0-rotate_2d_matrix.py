#!/usr/bin/python3
""" Module to rotatate a matrix 90 deg """


def rotate_2d_matrix(matrix):
    """ Rotates *matrix* by 90 deg """
    width = len(matrix[0])
    length = len(matrix)
    original_matrix = list()
    print(f">>> matrix is {length} × {width}")

    for i in range(length):
        original_matrix.insert(i, matrix[i].copy())
    for i in range(length):
        for j in range(width):
            matrix[i][j] = original_matrix[width - 1 - j][i]
