"""
CISC 131 Skyscraper Lab Problem 1-Akhil Kanayinkal (kana9520) and Rafael Caudillo (caud4682)
"""

import random

def main():
    """
    Add code here to individually test each of the methods you write.
    When you're done testing them, uncomment my code below and run it.
    """
    #Add your test code here
    #print(createRandomBorder(5))
    #printClues([1, 2, 3, 3, 3, 2, 1, 2, 2, 2, 3, 2])
    #printClues([3, 2, 4, 1, 1, 3, 3, 2, 2, 1, 2, 2, 3, 1, 2, 3])
    #print(generateRandomRow(5))
    #print(checkRow(generateRandomRow(5)))
    #print(checkBorder([2, 3, 1, 4, 5], 3, 1))



    #Sample code that generates a random problem and solution
    print("The random puzzle looks like:")
    border = createRandomBorder(4)
    printClues(border)
    print("")

    print("The random solution looks like:")
    board = createRandomSolution(4)
    printSoln(board)

    if checkSoln(border, board):
        print("The random solution is CORRECT")
    else:
        print("The random solution is NOT CORRECT")
    print("")

    #Some sample code that checks my own solution
    print("The puzzle looks like:")
    border = [3, 2, 4, 1, 1, 3, 3, 2, 2, 1, 2, 2, 3, 1, 2, 3]
    printClues(border)
    print("")
    print("Now I'm trying my own solution:")
    board = [[2, 3, 1, 4], [3, 4, 2, 1], [4, 1, 3, 2], [1, 2, 4, 3]]
    printSoln(board)

    if checkSoln(border, board):
        print("The solution is CORRECT")
    else:
        print("The solution is NOT CORRECT")


def createRandomBorder(size):
    """
    This function creates a random border with a specified size
    """
    #ADD YOUR CODE HERE
    arr = []
    for _i in range(size*4):
        arr.append(random.randint(1, size))
    return arr

def printClues(border):
    """
    This function prints out the border clues for the puzzle
    """
    #ADD YOUR CODE HERE
    top = []
    left = []
    right = []
    bottom = []
    for i in range(len(border)):
        if i < len(border)/4:
            top.append(border[i])
        elif i < len(border)/4*2:
            right.append(border[i])
        elif i < len(border)/4*3:
            bottom.append(border[i])
        else:
            left.append(border[i])
    bottom.reverse()
    left.reverse()
    space = " "
    num = len(border)//4 * 2 + 1
    for i in range(len(border)//4+2):
        if i == 0:
            print(" ", end="")
            for j in range(len(top)):
                print("{:>2d}".format(top[j]), end="")
            print()
        elif i < len(border)//(4**i):
            for j in range(len(top)):
                print("{:d}".format(left[j]), end=space*num)
                print("{:d}".format(right[j]))
        if i == len(border)//4+1:
            print(" ", end="")
            for j in range(len(top)):
                print("{:>2d}".format(bottom[j]), end="")
            print()

def generateRandomRow(size):
    """
    This function creates a random row with a specified size
    """
    #ADD YOUR CODE HERE
    lst = []
    for i in range(1, size + 1):
        lst.append(i)
    for i in range(size):
        index = random.randint(0, size - 1)
        val = lst[i]
        lst[i] = lst[index]
        lst[index] = val
    return lst

def checkRow(row):
    """
    This function checks whether a row is valid or not
    """
    #ADD YOUR CODE HERE
    for i in range(len(row)):
        for j in range(i + 1, len(row)):
            if row[i] == row[j]:
                return False
        if row[i] < 1 or row[i] > len(row):
            return False
    return True

def checkBorder(row, left, right):
    """
    This function checks whether a border is valid or not
    """
    #ADD YOUR CODE HERE
    l_count = 0
    r_count = 0
    max_height = 0
    for i in range(len(row)):
        if row[i] > max_height:
            l_count += 1
            max_height = row[i]
    max_height = 0
    for i in range(len(row) - 1, -1, -1):
        if row[i] > max_height:
            r_count += 1
            max_height = row[i]
    return l_count == left and r_count == right

def createRandomSolution(size):
    """
    This function creates and returns a random solution to a size x size puzzle.
    Each row will contain a random permutation of the numbers from 1 to size.
    """
    board = []
    for _i in range(size):
        board.append(generateRandomRow(size))
    return board

def printSoln(board):
    """
    This functions prints the board in a natural format.
    It expects board to be a 2-dimensional array.
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
        print("")

def checkSoln(border, board):
    """
    This function checks a potential solution to the skyscraper puzzle given by border
    to see if it valid.  The clues are given by the border parameter.  The function
    returns True if the solution is correct and False otherwise.
    """
    size = len(board)
    #check each row for duplicates & invalid values
    for i in range(len(board)):
        row = board[i]
        if not checkRow(row):
            return False
        if not checkBorder(row, border[-1-i], border[size+i]):
            return False

    #check each column for dupliates & invalid values
    for j in range(len(board)):
        col = [row[j] for row in board]
        if not checkRow(col):
            return False
        if not checkBorder(col, border[j], border[3*size-j-1]):
            return False

    return True

main()
