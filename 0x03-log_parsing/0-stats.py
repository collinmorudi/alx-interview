#!/usr/bin/env python3
"""log_parsing"""


import sys
import re
import signal


# Regular expression pattern to match the log format
log_pattern = (
    r'^(\d{1,3}\.){3}\d{1,3} - '
    r'\[(.*)\] "GET /projects/260 HTTP/1.1" '
    r'(\d{3}) (\d+)\s*$'
)


# Dictionary to store the count of each status code
status_code_count = {
    200: 0, 301: 0, 400: 0, 401: 0,
    403: 0, 404: 0, 405: 0, 500: 0
}


# Total file size
total_file_size = 0

# Line counter
line_count = 0


def signal_handler(sig, frame):
    """todo: add comment"""
    global total_file_size, status_code_count, line_count
    print_metrics()
    sys.exit(0)


def print_metrics():
    """todo: add comment"""
    global total_file_size, status_code_count
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_code_count.keys()):
        if status_code_count[status_code] > 0:
            print(f"{status_code}: {status_code_count[status_code]}")


def read_logs():
    """todo: add comment"""
    global total_file_size, status_code_count, line_count
    signal.signal(signal.SIGINT, signal_handler)
    for line in sys.stdin:
        line_count += 1
        match = re.match(log_pattern, line)
        if match:
            ip, date, status_code, file_size = match.groups()
            status_code = int(status_code)
            if status_code in status_code_count:
                status_code_count[status_code] += 1
                total_file_size += int(file_size)
        if line_count % 10 == 0 or line_count == 1:
            print_metrics()


if __name__ == '__main__':
    read_logs()
