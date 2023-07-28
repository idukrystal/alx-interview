#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generate Pascal's triangle with 'n' rows.

    Args:
        n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        list: A list of lists of integers representing Pascal's triangle.
              Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    # Initialize the triangle with the first row containing 1.
    triangle = [[1]]

    # Generate the remaining rows of the triangle.
    while len(triangle) < n:
        last_row = triangle[-1]
        next_row = [1]

        # Calculate the values for the next row
        for i in range(1, len(last_row)):
            next_row.append(last_row[i - 1] + last_row[i])

        next_row.append(1)
        triangle.append(next_row)

    return triangle
