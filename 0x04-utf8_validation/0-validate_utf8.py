#!/usr/bin/python3
"""
UTF-8 encoding
"""


def validUTF8(data):
    """
    method that determines if a given data set
    represents a valid UTF-8 encoding
    """
    bytes_rem = 0

    m_1 = 1 << 7
    m_2 = 1 << 6

    for n in data:

        m_byte = 1 << 7

        if bytes_rem == 0:

            while m_byte & n:
                bytes_rem += 1
                m_byte = m_byte >> 1

            if bytes_rem == 0:
                continue

            if bytes_rem == 1 or bytes_rem > 4:
                return False

        else:
            if not (n & m_1 and not (n & m_2)):
                    return False

        bytes_rem -= 1

    if bytes_rem == 0:
        return True

    return False
