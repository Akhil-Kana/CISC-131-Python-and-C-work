def printLine(num, sym):
    if num <= 1:
        print(sym)
    else:
        print(sym, end="")
        printLine(num-1, sym)

#printLine(5, "*")

def printRectangle(num1, num2, sym):
    printLine(num1, sym)

printRectangle(3, 4, "*")

def printSquare(num, sym):
    printRectangle(num1, num2, sym)

#printSquare(3, "*")
