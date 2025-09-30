"""
CISC 131 Problem 1 - Akhil Kanayinkal (kana9520) and Amelia Berry (berr8662)
"""

def promptInt(string):
    """
    This function determines whether the user's input is a valid number
    """
    is_num = False
    while not is_num:
        num = input(string)
        if num.isdigit() or (num[0] == "-" and num[1:].isdigit()):
            is_num = True
            return int(num)
        else:
            print("I'm sorry, that is not a valid number")

print(promptInt("How old are you? "))
