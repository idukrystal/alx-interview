from collections import defaultdict
import signal
import sys

# Define the status codes to track
status_codes = {200, 301, 400, 401, 403, 404, 405, 500}

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = defaultdict(int)
line_count = 0

def print_statistics(signal, frame):
    print("Total file size:", total_file_size)
    for code in sorted(status_codes):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")
    sys.exit(0)

signal.signal(signal.SIGINT, print_statistics)

try:
    for line in sys.stdin:
        parts = line.strip().split()
        if len(parts) != 10:
            continue
        
        ip, _, _, _, _, _, request, status_code_str, file_size_str = parts
        if not status_code_str.isdigit():
            continue
        
        status_code = int(status_code_str)
        if status_code not in status_codes:
            continue
        
        file_size = int(file_size_str)
        
        total_file_size += file_size
        status_code_counts[status_code] += 1
        line_count += 1
        
        if line_count % 10 == 0:
            print_statistics(None, None)

except KeyboardInterrupt:
    print_statistics(None, None)
