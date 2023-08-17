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
    ''' Resets a dictionaries values to 0 '''
    for key in dct:
        dct[key] = 0


def print_dict(dct):
    '''' Prints a dictionaries key,values line by line '''
    for key in dct:
        if dct[key] != 0:
            print(key+": "+str(dct[key]))


for line in stdin:
    line = line.split()
    if len(line) != 9 or line[7] not in status_codes:
        continue

    status_codes[line[7]] += 1
    lines_read += 1
    file_size += int(line[8])
    if lines_read == 10:
        lines_read = 0
        print(f"File Size: {file_size}")
        print_dict(status_codes)
        reset_dict(status_codes)
