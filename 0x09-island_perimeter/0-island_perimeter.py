#!/usr/bin/python3

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the given grid.
    
    Args:
        grid (list of list of int): The grid representing the island.
        
    Returns:
        int: The perimeter of the island.
    """
    if not grid:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    
    perimeter = 0
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4  # Each land cell contributes 4 to the perimeter
                
                # Check adjacent cells and subtract 1 for each adjacent land cell
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 1
                if row < rows - 1 and grid[row + 1][col] == 1:
                    perimeter -= 1
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 1
                if col < cols - 1 and grid[row][col + 1] == 1:
                    perimeter -= 1
                    
    return perimeter
