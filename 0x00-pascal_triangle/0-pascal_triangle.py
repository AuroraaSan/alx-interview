#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal triangle of n
    """
    # Check if n is less than or equal to 0
    if n <= 0:
        # Return an empty list if n is invalid
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]
    
    # Generate each row of the triangle
    for i in range(1, n):
        # Get the previous row
        prev_row = triangle[i - 1]
        # Calculate the new row based on the previous row
        new_row = [1] + [prev_row[j] + prev_row[j + 1] for j in range(len(prev_row) - 1)] + [1]
        # Append the new row to the triangle
        triangle.append(new_row)

    # Return the generated triangle
    return triangle