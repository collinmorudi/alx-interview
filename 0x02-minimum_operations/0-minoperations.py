#!/usr/bin/python3
"""
This module contains a function to calculate the fewest number
of operations needed to result in exactly n 'H' characters in the file.
"""


def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations needed to
    result in exactly n 'H' characters in the file.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The fewest number of operations needed, or 0 if n is
        impossible to achieve.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations


if __name__ == "__main__":
    print("Min # of operations to reach 4 characters:", minOperations(4))
    print("Min # of operations to reach 12 characters:", minOperations(12))
