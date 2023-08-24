#!/usr/bin/python3
"""  Write a method that determines if a
given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """ determines if a given data set
    represents a valid UTF-8 encoding.
    """
    rem_bytes = 0
    for byte in data:
        if rem_bytes == 0:
            if byte in range(1, 128):
                rem_bytes = 0
            elif byte in range(192, 224):
                rem_bytes = 1
            elif byte in range(224, 240):
                rem_bytes = 2
            elif byte in range(240, 248):
                rem_bytes = 3
            else:
                return False
        else:
            if byte not in range(128, 192):
                return False
            rem_bytes -= 1
    return rem_bytes == 0
