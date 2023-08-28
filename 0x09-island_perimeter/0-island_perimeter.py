#!/usr/bin/python3

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the given grid.
    
    Args:
        grid (list of list of int): The grid representing the island.
        
    Returns:
        int: The perimeter of the island.
    """
    total_perimeter = 0
    prev_row_index_ones = []

    for row in grid:
        current_row_index_ones = []
        current_row_perimeter = 0

        for index, val in enumerate(row):
            if val == 0:  # Water cell
                continue
            else:  # Land cell
                try:
                    # Check if the previous cell in this row is a land cell
                    if index - 1 == current_row_index_ones[-1]:
                        current_row_perimeter += 2
                    else:
                        current_row_perimeter += 4
                except IndexError:  # First land cell in the row
                    current_row_perimeter += 4
                
                if index in prev_row_index_ones:
                    current_row_perimeter -= 2  # Adjacent cells, subtract 2 from perimeter
                current_row_index_ones.append(index)
        
        prev_row_index_ones = current_row_index_ones
        total_perimeter += current_row_perimeter

    return total_perimeter
