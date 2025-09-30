"""
CISC 131 Problem 2 - Akhil Kanayinkal (kana9520)
"""

import math

def countDigits(num, digit):
    """
    This functions finds the number of a desired digit within a number
    """
    count = 0
    length = math.ceil(math.log10(num))
    if num == 1:
        count+=1
    else:
        for i in range(1,length+1):
            if math.floor(int(num % (10**i)//(10**(i-1)))) == digit:
                count+=1
    return count

print(countDigits(42354, 4))
print(countDigits(42354, 9))
