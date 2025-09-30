"""
CISC 131 Problem 1 - Akhil Kanayinkal (kana9520) and Sean Marlow (marl9416)
"""

def isPalindrome(string):
    """
    This function checks whether a string is a palindrome or not
    """
    count = 0
    for i in range(len(string)//2):
        if string[i] == string[len(string)-i-1]:
            count += 1
        else:
            count += 0
    if count == (len(string)//2):
        return True
    else:
        return False


print(isPalindrome("deed"))
print(isPalindrome("racecar"))
print(isPalindrome("helloh"))
