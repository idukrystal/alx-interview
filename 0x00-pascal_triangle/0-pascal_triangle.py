def pascal_triangle(n):
    if n <= 0:
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
