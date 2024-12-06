# 0x09. Island Perimeter

## Algorithm
* Python

**Weight:** 1

**Project start:** Dec 2, 2024 6:00 AM

**Project end:** Dec 6, 2024 6:00 AM

**Checker released:** Dec 3, 2024 6:00 AM

**Auto review:** At the deadline

## Task: 0. Island Perimeter

**Mandatory**

Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in `grid`:

* `grid` is a list of lists of integers:
    * 0 represents water
    * 1 represents land
* Each cell is square, with a side length of 1
* Cells are connected horizontally/vertically (not diagonally).
* `grid` is rectangular, with its width and height not exceeding 100
* The grid is completely surrounded by water
* There is only one island (or nothing).
* The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

**Example:**

```python
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
