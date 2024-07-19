#!/usr/bin/python3
"""
A script for parsing HTTP request logs.
"""
import sys
import re

def extract_input(input_line):
    """
    Extracts sections of a line of an HTTP request log.
    """
    pattern = (
        r'(?P<ip>\S+) - \[(?P<date>.*?)\] "(?P<request>.*?)" (?P<status_code>\d{3}) (?P<file_size>\d+)'
    )
    match = re.match(pattern, input_line)
    if match:
        return {
            'status_code': match.group('status_code'),
            'file_size': int(match.group('file_size'))
        }
    return None

def print_statistics(total_file_size, status_counts):
    """
    Prints the accumulated statistics of the HTTP request log.
    """
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")

def update_metrics(line, total_file_size, status_counts):
    """
    Updates the metrics from a given HTTP request log.
    """
    log_entry = extract_input(line)
    if log_entry:
        total_file_size += log_entry['file_size']
        status_code = log_entry['status_code']
        if status_code in status_counts:
            status_counts[status_code] += 1
        else:
            status_counts[status_code] = 1
    return total_file_size

def run():
    """
    Starts the log parser.
    """
    total_file_size = 0
    status_counts = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
    line_count = 0

    try:
        for line in sys.stdin:
            total_file_size = update_metrics(line.strip(), total_file_size, status_counts)
            line_count += 1
            if line_count % 10 == 0:
                print_statistics(total_file_size, status_counts)
    except KeyboardInterrupt:
        print_statistics(total_file_size, status_counts)
        sys.exit(0)
    print_statistics(total_file_size, status_counts)

if __name__ == '__main__':
    run()

