"""
CISC 131 Problem 2 - Akhil Kanayinkal (kana9520) and Sean Marlow (marl9416)
"""

def isCapital(letter):
    """
    This function converts the index of a string into a capital
    """
    upper_case = ord(letter) - 32
    return chr(upper_case)

def acronym(string):
    """
    This function converts a string into an acronym
    """
    finished_string = ""
    for i in range(len(string)):
        if ord(string[i]) == 32:
            if ord(string[i+1]) != 32:
                if ord(string[i+1]) < 97:
                    finished_string += string[i+1]
                else:
                    finished_string += isCapital(string[i+1])
        elif i == 0:
            if ord(string[i]) < 97:
                finished_string += string[i]
            else:
                finished_string += isCapital(string[i])
    return finished_string

print(acronym("My name is akhil"))
print(acronym("    aAaPle kEeeps   the Doctor away"))
