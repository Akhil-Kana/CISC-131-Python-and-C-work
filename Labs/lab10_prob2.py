"""
CISC 131 Problem 2 - Akhil Kanayinkal (kana9520) and Amelia Berry (berr8662)
"""

def syracuse(num):
    """
    This funcion returns the syracruse sequence of a number
    """
    is_one = False
    string = str(num) + ", "
    while not is_one:
        if num % 2 == 0:
            num = num//2
            string += str(num) + ", "
            if num == 1:
                is_one = True
                return string[:-2]
        else:
            num = 3*num + 1
            string += str(num) + ", "
            if num == 1:
                is_one = True
                return string[:-2]

print(syracuse(5))
