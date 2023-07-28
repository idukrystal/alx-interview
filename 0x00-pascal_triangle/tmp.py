#!/usr/bin/python3
"""Module to create a pascals triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle with 'n' rows.

    Args:
        n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        list: A list of lists of integers representing Pascal's triangle.
              Returns an empty list if n <= 0.
    """
    
    if type(n) is not int or n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) < n:
        last_row = triangle[-1]
        next_row = [1]

        for i in range(1, len(last_row)):
            next_row.append(last_row[i - 1] + last_row[i])

        next_row.append(1)
        triangle.append(next_row)

    return triangle
