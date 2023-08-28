#!/usr/bin/python3

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the given grid.
    
    Args:
        grid (list of list of int): The grid representing the island.
        
    Returns:
        int: The perimeter of the island.

    Algorithm:
        1. Input: The function takes a 2D grid as input, where each cell is either 0 (water) or 1 (land).
        2. Initialization: Initialize a variable perimeter to keep track of the cumulative perimeter of the island. Also, determine the number of rows and columns in the grid.
        3. Iterating Through Rows and Columns: Iterate through each cell in the grid.
            a. For each cell (identified by its row and column index):
                If the cell's value is 0, continue to the next cell (it's water).
                If the cell's value is 1 (land):
                    Add 4 to the perimeter to account for the four sides of the cell.
                    Check if there's a cell to the right (within the same row) and if that cell is also a land cell. If it is, subtract 2 from the perimeter (since the right side of the current cell is shared with the adjacent cell).
                    Check if there's a cell below (in the next row) and if that cell is also a land cell. If it is, subtract 2 from the perimeter (since the bottom side of the current cell is shared with the adjacent cell).
        Return Result: After iterating through all cells, return the final perimeter as the result.
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
