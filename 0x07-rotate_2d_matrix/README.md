# 0. Rotate 2D Matrix

This project implements an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise.

## Algorithm

The rotation is achieved in two steps:

1. **Transpose the matrix:** Swap rows and columns.
2. **Reverse each row:** Reverse the order of elements in each row.

## Example Usage

```python
>>> matrix = [[1, 2, 3],
...           [4, 5, 6],
...           [7, 8, 9]]
>>> rotate_2d_matrix(matrix)
>>> print(matrix)
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
