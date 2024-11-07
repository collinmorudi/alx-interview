#!/usr/bin/python3
"""
N Queens Puzzle: Solve the N Queens problem using backtracking.
"""


import sys


def print_solution(board):
    """Prints the solution in the required format."""
    print([[i, row.index(1)] for i, row in enumerate(board)])


def is_safe(board, row, col):
    """Checks if placing a queen at board[row][col] is safe."""
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col):
    """Uses backtracking to solve the N Queens problem."""
    if col >= len(board):
        print_solution(board)
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens(board, col + 1)
            board[i][col] = 0


def main():
    """Main function to parse arguments and initiate the N Queens solution."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * n for _ in range(n)]
    solve_nqueens(board, 0)


if __name__ == "__main__":
    main()
