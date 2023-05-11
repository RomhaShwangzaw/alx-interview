#!/usr/bin/python3
"""Log parsing module"""
import sys


st_code = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
total_size = 0
line_counter = 0

try:
    for line in sys.stdin:
        words = line.split()
        if len(words) > 4:
            if words[-2] in st_code.keys():
                st_code[words[-2]] += 1
            total_size += int(words[-1])
            line_counter += 1

        if line_counter == 10:
            print("File size: {}".format(total_size))
            for code, count in sorted(st_code.items()):
                if count > 0:
                    print("{}: {}".format(code, count))
            line_counter = 0

except Exception:
    pass

finally:
    print("File size: {}".format(total_size))
    for code, count in sorted(st_code.items()):
        if count > 0:
            print("{}: {}".format(code, count))
