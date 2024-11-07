# 0x05. N Queens

This project implements a solution to the classic N Queens puzzle. The goal of the puzzle is to place `N` queens on an `N x N` chessboard such that no two queens can attack each other.

## Concepts

- **Backtracking**: This algorithm explores each possible solution and backtracks when a solution cannot be completed.
- **Recursion**: The solution employs recursion to attempt placing queens on each column one by one.
- **List Manipulation**: The program manipulates lists to represent the board and store queen positions.
- **Command Line Arguments**: The solution accepts an integer `N` via the command line to determine the board size.

## Requirements

- Python 3.4.3
- Ubuntu 20.04 LTS
- Code style follows PEP 8 (version 1.7.\*)

## Usage

The program takes a single argument, `N`, which must be an integer greater than or equal to 4. It prints each solution as a list of `[row, col]` positions representing the locations of queens on the board.

### Example

```bash
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

