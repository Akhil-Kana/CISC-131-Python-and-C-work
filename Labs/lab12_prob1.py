"""
CISC 131 Problem 1 - Akhil Kanayinkal (kana9520)
"""

def sortBinary(lst):
    """
    This function recursively sorts binary numbers in ascending order
    """
    if len(lst) == 0:
        return []
    else:
        return [0] + sortBinary(lst[1:]) if lst[0] == 0 else sortBinary(lst[1:]) + [1]

print(sortBinary([0,1,0,1]))
