#!/usr/bin/python3
"""
Contains island_perimeter function
"""

def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid
    Args:
        grid: 2D list of integers containing 0 (water) or 1 (land)
    Return:
        the perimeter of the island
    """
    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                perimeter += 4

                # Check the top
                if row - 1 >= 0 and grid[row - 1][col] == 1:
                    perimeter -= 1

                # Check the left
                if col - 1 >= 0 and grid[row][col - 1] == 1:
                    perimeter -= 1

                # Check the bottom
                if row + 1 < len(grid) and grid[row + 1][col] == 1:
                    perimeter -= 1

                # Check the right
                if col + 1 < len(grid[0]) and grid[row][col + 1] == 1:
                    perimeter -= 1

    return perimeter
