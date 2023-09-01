#!/usr/bin/python3
"""
0-island_perimeter
"""

def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid.
    
    Args:
    grid (List[List[int]]): The grid representing the island.
    
    Returns:
    int: The perimeter of the island.
    """
    perimeter = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4  # Each land cell contributes 4 to the perimeter
                
                # Check the adjacent cells to subtract the shared sides
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtracting the top side from both cells
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Subtracting the left side from both cells
    
    return perimeter
    
