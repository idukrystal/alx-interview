
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
        byte = byte & 255
        if rem_bytes == 0:
            if byte >> 7 == 0:
                rem_bytes = 0
            elif byte >> 5 == 0b110:
                rem_bytes = 1
            elif byte  >> 4 == 0b1110:
                rem_bytes = 2
            elif byte >> 3 == 0b11110:
                rem_bytes = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            rem_bytes -= 1
    return rem_bytes == 0

#data = [0xF4, 0x8F, 0xBF, 0xBD, 0xF0, 0x90, 0x80, 0x80] 
#print(validUTF8(data))
# print(x >> 7)
