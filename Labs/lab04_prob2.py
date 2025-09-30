"""
CISC 131 Problem 2 - Akhil Kanayinkal (kana9520) and Nathan Kostynick (kost6288)
"""
def main():
    """
    This is the main function that calls all of the functions below
    """

    printLine(5, "$")
    printRect(3, 5, "&")
    printUpTriangle(3, "T")
    printDownTriangle(5, "#")
    printHills(4, "H", "!")

def printLine(num, sym): #sym = symbol
    """
    This function prints out a line of symbols
    """

    for _i in range(num):
        print(sym, end="")
    print("")

def printRect(width, height, sym):
    """
    This function prints out a line of symbols in the shape of a rectangle
    """

    for _i in range(height):
        printLine(width, sym)

def printUpTriangle(width, sym):
    """
    This function prints out a line of symbols in the shape of an ascending triangle
    """
    for i in range(width):
        printLine(i+1, sym)

def printDownTriangle(width, sym):
    """
    This function prints out a line of symbols in the shape of a descending triangle
    """
    for i in range(width, 0, -1):
        printLine(i, sym)

def printHills(num, sym1, sym2):
    """
    This function prints out a line of symbols in the shape of a ascending triangle
    """
    for i in range(num):
        printUpTriangle(i+1, sym1)
        printDownTriangle(i+1, sym2)

main()
