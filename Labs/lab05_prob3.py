"""
CISC 131 Problem 3 - Akhil Kanayinkal (kana9520)
"""

def symbolDesign(width, symbol1, symbol2):
    """
    This function prints out a upper and lower triangle from two symbols respectively
    """
    for i in range(1, width):
        for j in range(width):
            if i > j:
                print(symbol1, end="")
            else:
                print(symbol2, end="")
        print()


symbolDesign(5, "|", "/")
symbolDesign(8, "!", "?")
