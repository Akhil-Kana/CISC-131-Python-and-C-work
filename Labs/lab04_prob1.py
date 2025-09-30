"""
CISC 131 Problem 1 - Akhil Kanayinkal (kana9520) and Nathan Kostynick (kost6288)
"""

def main():
    """
    This is the main function that calls factorialTable
    """

    factorialTable(10)

def factorial(num):
    """
    This function finds the factorial of a number
    """

    answer = 1
    for i in range(num):
        answer += answer * i
    return answer

def factorialTable(num):
    """
    This function prints out a table of factorials and calls the factorial function
    """

    for i in range(num+1):
        print(i, end="")
        print("! = ", end="")
        print(factorial(i))

main()
