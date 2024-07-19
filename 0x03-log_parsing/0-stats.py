#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import sys
import signal

# Initialize variables
total_size = 0
status_counts = {}
line_count = 0

def print_stats():
    """
    Print the total file size and the count of each status code.
    """
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        print(f"{status}: {status_counts[status]}")

def signal_handler(sig, frame):
    """
    Handle keyboard interruption (CTRL + C).
    """
    print_stats()
    sys.exit(0)

# Assign the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    line_count += 1
    parts = line.split()

    """
    Skip lines that do not match the expected format.
    """
    if len(parts) < 7:
        continue

    try:
        """
        Extract status code and file size from the line.
        """
        status_code = int(parts[-2])
        file_size = int(parts[-1])
    except ValueError:
        continue

    """
    Update the total file size.
    """
    total_size += file_size

    """
    Update the count for the status code.
    """
    if status_code in status_counts:
        status_counts[status_code] += 1
    else:
        status_counts[status_code] = 1

    """
    Print statistics after every 10 lines.
    """
    if line_count % 10 == 0:
        print_stats()

"""
Print final statistics if there are fewer than 10 lines.
"""
print_stats()
```
