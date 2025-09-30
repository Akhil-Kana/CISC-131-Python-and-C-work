"""
CISC 131 Problem 1 - Akhil Kanayinkal (kana9520) and Kaden Stewart (stew3234)
"""

def main():
    """
    This is the main function that calls the function speedingTicketFine
    """
    speedingTicketFine(30, 35)
    speedingTicketFine(70, 90)
    speedingTicketFine(45, 40)

def speedingTicketFine(speed_limit, clocked_speed):
    """
    This function calculates the fine for going over the speed limit
    """
    fine = 0
    if clocked_speed > speed_limit:
        fine += 50 + (5 * (clocked_speed % speed_limit))
        if clocked_speed >= 90:
            fine += 200
        print("Your fine is $" + str(fine))
    else:
        print("You are driving a legal speed!")

main()
