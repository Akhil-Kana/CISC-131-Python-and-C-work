"""
CISC 131 Problem 4 - Akhil Kanayinkal (kana9520)
"""
import math

def convertBinary(num):
    """
    This function converts a number into a binary number that's a string
    """
    string = ""
    if num == 1:
        string += str(num)
    else:
        for _i in range(math.floor(math.sqrt(num))+1):
            string = str(num%2) + string
            num//=2
    return string

print(convertBinary(16))
print(convertBinary(3))
