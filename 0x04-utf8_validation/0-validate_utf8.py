#!/usr/bin/python3
"""  Write a method that determines if a
given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """ determines if a given data set
    represents a valid UTF-8 encoding.
    """
    if not isinstance(data, list):
        return False
    for i in data:
        if not isinstance(i, int):
            return False
    data = iter(data)
    rem_bytes = 0
    try:
        byte = next(data)
        while byte:
            if byte in range(128):
                rem_bytes = 1
            elif byte in range(192, 224):
                rem_bytes = 2
            elif byte in range(224, 240):
                rem_bytes = 3
            elif byte in range(240, 248):
                rem_bytes = 4
            else:
                return False
            rem_bytes -= 1
            while rem_bytes > 0:
                byte = next(data)
                if byte not in range(128, 192):
                    return False
                rem_bytes -= 1
            byte = next(data)

    except StopIteration:
        if rem_bytes == 0:
            return True
        return False
