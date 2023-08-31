#!/usr/bin/python3

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the given grid.
    
    Args:
        grid (list of list of int): The grid representing the island.
        
    Returns:
        int: The perimeter of the island.
    """
    perimeter=0

    rows = len(grid)
    cols = len(grid[0])

    for row_index, row in enumerate(grid):
        for col_index, val in enumerate(row):
            if val == 1:
                perimeter += 4  # Start with 4 for each land cell

                # Check the right cell
                next_col = col_index + 1
                if next_col < cols and row[next_col] == 1:
                    perimeter -= 2

                # Check the below cell
                next_row = row_index + 1
                if next_row < rows and grid[next_row][col_index] == 1:
                    perimeter -= 2

    return perimeter
