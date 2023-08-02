#!/usr/bin/python3
"""N queens puzzle solver"""

import sys

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]"""

    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def nqueens_helper(board, col, solutions):
    """Recursive helper function to find all solutions for N queens"""

    # Base case: If all queens are placed
    if col == len(board):
        solutions.append([[i, row.index(1)] for i, row in enumerate(board)])
        return

    for row in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            nqueens_helper(board, col + 1, solutions)
            board[row][col] = 0

def nqueens(N):
    """Find all possible solutions for N queens"""

    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    nqueens_helper(board, 0, solutions)

    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

