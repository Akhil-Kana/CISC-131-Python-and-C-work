"""
CISC 131 Problem 2 - Akhil Kanayinkal (kana9520)
"""

def reverseString(string):
    """
    This function recusively reverses a string
    """
    return "" if len(string) == 0 else string[-1] + reverseString(string[:-1])

print(reverseString("Tommie"))
