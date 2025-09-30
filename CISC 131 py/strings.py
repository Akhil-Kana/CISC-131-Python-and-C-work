"""
CISC 131
Topic: Strings
Author: Dr. Miracle
"""
def main():
    """
    This function tests the lowerCase function.
    """
    print(lowerCase('Hi'))
    print(lowerCase('HI'))
    print(lowerCase('hello'))

def lowerCase(my_str):
    """
    This function returns the lower-case version
    of the string my_str
    """
    str_so_far = ""

    for index in range(len(my_str)):
        current_ascii = ord(my_str[index])
        if current_ascii >= ord('A') and current_ascii <= ord('Z'):
            #the character is upper-case
            str_so_far = str_so_far + chr(current_ascii + 32)
        else:
            #all other characters
            str_so_far = str_so_far + my_str[index]

    return str_so_far

main()
