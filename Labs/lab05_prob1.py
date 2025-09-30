"""
CISC 131 Problem 1 - Akhil Kanayinkal (kana9520)
"""

def isPrime(num):
    """
    This function determines whether a number is a prime number or not
    """
    if num % 2 != 0 and num % 3 != 0:
        return True
    else:
        return False

print(isPrime(7))
print(isPrime(6))
print(isPrime(3))
print(isPrime(4))
