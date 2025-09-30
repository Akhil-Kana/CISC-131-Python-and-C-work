"""
CISC 131 Problem 3 - Akhil Kanayinkal (kana9520) and Sean Marlow (marl9416)
"""


def myReverse(input_num):
    """
    This function reverses the order of any number between 0 through 9999
    """

    one_digit = int(input_num % 10)
    ten_digit = int(((input_num % 100) - one_digit) / 10)
    hundred_digit = int(((input_num % 1000) - (input_num % 100)) / 100)
    thousand_digit = int((input_num - (input_num % 1000)) / 1000)
    one_digit *= 1000
    ten_digit *= 100
    hundred_digit *= 10
    total = one_digit + ten_digit + hundred_digit + thousand_digit
    return total

print(myReverse(1234))
