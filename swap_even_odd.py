"""Good morning! Here's your coding interview problem for today.

This problem was asked by Cisco.

Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.

For example, 10101010 should be 01010101. 11100010 should be 11010001.

Bonus: Can you do this in one line?"""

def reverse_bytes(b):
    b = list(str(b))
    for i in range(0,8,2):
        b[i],b[i+1] = b[i+1], b[i]
    return int(''.join(b))

print(reverse_bytes(11100010))
