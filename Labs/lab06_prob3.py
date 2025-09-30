"""
CISC 131 Problem 3 - Akhil Kanayinkal (kana9520) and Sean Marlow (marl9416)
"""

def swapEnc(key, string):
    """
    This function encrypts a string with the transposition cipher
    """
    end_string = ""
    for i in range(len(string)):
        end_string += string[(key-i)%len(string)]
    return end_string

def swapDec(key, string):
    """
    This function decrypts a string encrypted by the transposition cipher
    """
    return swapEnc(len(string) + key, string)

print(swapEnc(4, "strong wind"))
print(swapDec(4, "nortsdniw g"))

print(swapEnc(18, "hello world"))
print(swapDec(18, "ow ollehdlr"))
