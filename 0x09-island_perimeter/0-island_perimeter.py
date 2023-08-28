#!/usr/bin/python3

def island_perimeter(grid):
    total_perimeter=0
    prev_row_index_ones=[]

    for row in grid:
        current_row_index_ones=[]
        current_row_perimeter=0

        for index, val in enumerate(row):
            if val==0:
                continue
            else:
                try:
                    if index-1 == current_row_index_ones[-1]:
                        current_row_perimeter += 2
                    else:
                        current_row_perimeter += 4
                except:
                    current_row_perimeter += 4
                if index in prev_row_index_ones:
                    current_row_perimeter -= 2
                current_row_index_ones.append(index)
        prev_row_index_ones=current_row_index_ones
        total_perimeter += current_row_perimeter

    return total_perimeter
