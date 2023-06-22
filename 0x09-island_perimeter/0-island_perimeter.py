#!/usr/bin/python3
""" Island Perimeter Module
"""


def island_perimeter(grid):
    """ Calculates perimeter of an island described in `grid`
    Params:
      @grid: a list of list of integers
        - 0 represents water
        - 1 represents land
        - Each cell is square, with a side length of 1
        - Cells are connected horizontally/vertically (not diagonally)
        - grid is rectangular, with its width and height not exceeding 100
    Assumptions:
      * The grid is completely surrounded by water
      * There is only one island (or nothing)
      * The island doesn’t have “lakes” (water inside that isn’t
        connected to the water surrounding the island)
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4
                if grid[i - 1][j] and grid[i - 1][j] == 1:
                    perimeter -= 1
                if grid[i + 1][j] and grid[i + 1][j] == 1:
                    perimeter -= 1
                if grid[i][j - 1] and grid[i][j - 1] == 1:
                    perimeter -= 1
                if grid[i][j + 1] and grid[i][j + 1] == 1:
                    perimeter -= 1
    return perimeter
