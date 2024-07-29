#!/usr/bin/python3
""" UTF-8 validation """


def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the significant bits of a byte
    mask1 = 1 << 7
    mask2 = 1 << 6

    # Iterate over each byte in the data
    for byte in data:
        # Get the 8 least significant bits of the byte
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte & mask1) == 0:
                continue
            elif (byte & mask1) and (byte & mask2):
                mask = 1 << 7
                while byte & mask:
                    num_bytes += 1
                    mask = mask >> 1
                if num_bytes == 1 or num_bytes > 4:
                    return False
        else:
            # Check if the byte is a valid continuation byte
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
