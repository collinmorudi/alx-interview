#!/usr/bin/env python3
"""minimum operations"""


def minOperations(n):
    """
    TODO: add doc strings
    """
    if n <= 1:
        return 0

    min_operations = 0
    current_length = 1
    clipboard = 0

    while current_length < n:
        if n % current_length == 0:
            clipboard = current_length
            min_operations += 1  # Copy All operation
            current_length += clipboard
            min_operations += 1  # Paste operation
        else:
            current_length += clipboard
            min_operations += 1  # Paste operation

    return min_operations
