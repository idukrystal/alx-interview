#!/usr/bin/python3
""" an alx-interview project """


def island_perimeter(grid):
    """ Calcultes the pefimeter of a bit island """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            square = grid[i][j]
            square_perimeter = 4
            if square == 1:
                if i != 0:
                    if grid[i-1][j] == 1:
                        square_perimeter -= 1
                if i != (len(grid) - 1):
                    if grid[i+1][j] == 1:
                        square_perimeter -= 1
                if j != 0:
                    if grid[i][j-1] == 1:
                        square_perimeter -= 1
                if j != (len(grid[i]) - 1):
                    if grid[i][j+1] == 1:
                        square_perimeter -= 1
                perimeter += square_perimeter
    return perimeter
