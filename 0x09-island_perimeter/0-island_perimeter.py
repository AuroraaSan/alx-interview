#!/usr/bin/python3

""" Contains makeChange function"""


def island_perimeter(grid):
    """
    Returns: perimeter of island

    """
    perimeter = 0
    for row in range(len(grid)):
      for col in range(len(grid[0])):
        if grid[row][col] == 1:
          perimeter +=4
          if (row-1 >= 0 and grid[row-1][col]== 1 ):
            perimeter -= 1
          if (col -1 >= 0 and grid[row][col - 1] == 1 ):
            perimeter -= 1
          if (row + 1 >= 0 and grid[row + 1][col] == 1):
            perimeter -= 1
          if (col + 1 >= 0 and grid[row][col + 1] == 1):
            perimeter -= 1
    return perimeter
