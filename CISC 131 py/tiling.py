def tiling():
    print("What size board would you like? (Width) ", end="")
    width = int(input())
    print("What size board would you like? (Height) ", end="")
    height = int(input())
    print("What pattern would you like (1-3): ", end="")
    pattern = int(input())
    board = []
    if pattern == 1:
        for row in range(height):
            board.append([])
            for column in range(width):
                if (row + column)%2 == 0:
                    board[row].append('O')
                else:
                    board[row].append('X')
    elif pattern == 2:
        for row in range(height):
            board.append([])
            for column in range(width):
                if (row + column)%3 == 0:
                    board[row].append('O')
                else:
                    board[row].append('X')
    elif pattern == 3:
        for row in range(height):
            board.append([])
            for column in range(width):
                if column % 2 == 0:
                    board[row].append('O')
                else:
                    board[row].append('X')
    printBoard(board)

def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end="")
        print()

tiling()
