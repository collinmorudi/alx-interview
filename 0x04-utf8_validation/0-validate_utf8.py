#!/usr/bin/python3
"""
Module for UTF-8 Validation.

This module contains a function to check if a list of integers represents a
valid UTF-8 encoding. Each integer in the list represents a byte in the
encoding sequence.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    UTF-8 encoding can use 1 to 4 bytes per character:
    - 1-byte character starts with a 0 bit in the most significant position.
    - Multi-byte characters start with specific patterns:
        - 2-byte characters start with '110' followed by '10' for the next byte
        - 3-byte characters start with '1110' followed by '10' for each
        following byte.
        - 4-byte characters start with '11110' followed by '10' for each
        following byte.

    Args:
        data (list of int): A list of integers where each integer represents
        a byte
                            (8 least significant bits are considered).

    Returns:
        bool: True if data is a valid UTF-8 encoding, False otherwise.
    """
    n_bytes = 0

    for num in data:
        byte = num & 0xFF  # Consider only the last 8 bits

        if n_bytes == 0:
            # Check for leading byte pattern based on the UTF-8 rules.
            if (byte >> 5) == 0b110:  # 2-byte character
                n_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                n_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                n_bytes = 3
            elif (byte >> 7):  # 1-byte character must start with 0
                return False
        else:
            # Check that subsequent bytes start with '10' in the two
            # most significant bits.
            if (byte >> 6) != 0b10:
                return False
            n_bytes -= 1

    # If n_bytes is 0, all bytes were valid for UTF-8 encoding
    return n_bytes == 0
