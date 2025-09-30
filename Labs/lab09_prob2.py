"""
CISC 131 Problem 2 - Akhil Kanayinkal (kana9520)
"""
import random

def createBoard(dims):
    """
    This function creates a board randomly filled with True or False
    """
    board = []
    for i in range(dims):
        board.append([])
        for _j in range(dims):
            if random.randint(0,1) == 0:
                board[i].append(bool(0))
            else:
                board[i].append(bool(1))
    return board

def printBoard(board):
    """
    This function prints out a board
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]:
                print("@", end="")
            else:
                print("0", end="")
        print()

def winningBoard(board):
    """
    This function determines whether a board is a winning board or not
    """
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]:
                count += 1
            board[i][j] = not board[i][j]
        if count > 0:
            return False
    return True

def makeMove(board, x, y):
    """
    This function turns off or on a light with specific coordinates on the board
    """
    _len = len(board)
    if x > _len or y > _len or x <= 0 or y <= 0:
        return False
    board[_len-y][x-1] = not board[_len-y][x-1]
    if y - 1 > 0:
        board[_len-y+1][x-1] = not board[_len-y+1][x-1]
    if y < _len:
        board[_len-y-1][x-1] = not board[_len-y-1][x-1]
    if x - 1 > 0:
        board[_len-y][x-2] = not board[_len-y][x-2]
    if x < _len:
        board[_len-y][x] = not board[_len-y][x]
    return True

def playLightsOut():
    """
    This function allows someone to play the game Lights Out.
    Call this function AFTER writing AND TESTING the 4 functions
    described in the lab description on Canvas.
    """
    #Create the board
    dim = int(input("What size board do you want to start with? "))
    board = createBoard(dim)
    printBoard(board)
    #This variable controls the while loop
    keep_going = True
    #Continue as long as the user wants to keep going.
    while keep_going:
        #Get the next coordinates
        x = int(input("Enter an x coordinate: "))
        y = int(input("Enter an y coordinate: "))
        #Make the move and print the board.
        if not makeMove(board, x, y):
            print("Not a valid move")
        printBoard(board)
        #Check if the user won.
        if winningBoard(board):
            print("You won!!!")
            keep_going = False
        #If they didn't win ask if they want to keep going.
        else:
            input_string = input("Do you want to keep going (Y/N)? ")
            if input_string != "Y" and input_string != "y":
                keep_going = False

#print(createBoard(5))
#printBoard(createBoard(5))
#print(winningBoard(createBoard(5)))
playLightsOut()
