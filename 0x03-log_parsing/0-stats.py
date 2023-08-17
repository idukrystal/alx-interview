#!/usr/bin/python3
''' Alx project module on log parsing '''

from sys import stdin

status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

lines_read = 0
file_size = 0


def reset_dict(dct):
    ''' Resets a dictionaries values to 0'''
    for key in dct:
        dct[key] = 0


def print_dict(dct):
    '''' Prints a dictionaries key,values line by line '''
    for key in dct:
        if dct[key] != 0:
            print(key+": "+str(dct[key]))


def print_stats():
    ''' prints matrices statistics '''
    print(f"File size: {file_size}")
    print_dict(status_codes)


try:
    for line in stdin:
        line = line.split()
        if len(line) != 9:
            continue
        if line[7] in status_codes:
            status_codes[line[7]] += 1
        lines_read += 1
        file_size += int(line[8])
        if lines_read == 10:
            lines_read = 0
            print_stats()
except KeyboardInterrupt:
    print_stats()

else:
    print_stats()
