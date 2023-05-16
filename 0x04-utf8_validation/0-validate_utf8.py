#!/usr/bin/python3
"""UTF-8 Validation Module"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Return:
        True if data is a valid UTF-8 encoding, else return False

    Description:
        * A character in UTF-8 can be 1 to 4 bytes long
        * The data set can contain multiple characters
        * The data will be represented by a list of integers
        * Each integer represents 1 byte of data, therefore only
          the 8 least significant bits of each integer are handled
    """
    num_bytes = 1

    for d in data:
        d = d & 0b011111111
        if num_bytes == 1:
            if d >> 5 == 0b110:
                # check if it's a 2-byte character
                num_bytes = 2
            elif d >> 4 == 0b1110:
                # check if it's a 3-byte character
                num_bytes = 3
            elif d >> 3 == 0b11110:
                # check if it's a 4-byte character
                num_bytes = 4
            elif d >> 7 == 0b1:
                # check if it's an invalid byte
                return False
        else:
            if d >> 6 != 0b10:
                # check if it's not a continuation byte
                return False
            num_bytes -= 1

    return num_bytes == 1
