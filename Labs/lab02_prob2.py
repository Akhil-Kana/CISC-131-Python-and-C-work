"""
CISC 131 Problem 2 - Akhil Kanayinkal (kana9520) and Sean Marlow (marl9416)
"""

import math

def numBits(n_val):
    """
This functions is the change of base formula. It will find the number of bits that you need.
    """
    bit = math.log10(n_val)/math.log10(2)
    return math.ceil(bit)

print(numBits(8))
