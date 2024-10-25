#!/usr/bin/python3
"""Log parsing script that reads from stdin and computes metrics"""

import sys
import signal

# Initialize variables to store total file size and status codes
total_file_size = 0
status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
line_count = 0


def print_stats():
    """Print accumulated statistics"""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C)"""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        # Skip lines that don't have the correct number of parts
        if len(parts) < 7:
            continue

        # Try to extract file size and status code
        try:
            file_size = int(parts[-1])
            status_code = parts[-2]
        except (ValueError, IndexError):
            continue

        # Update total file size and status code count if valid
        total_file_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1

        # Every 10 lines, print statistics
        if line_count % 10 == 0:
            print_stats()

except Exception:
    pass

finally:
    print_stats()
