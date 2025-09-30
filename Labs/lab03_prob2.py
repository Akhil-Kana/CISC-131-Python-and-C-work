"""
CISC 131 Problem 2 - Akhil Kanayinkal (kana9520) and Kaden Stewart (stew3234)
"""

def main():
    """
    This is the main function that calls leapYear, validDate, and calDayNum
    """
    print(leapYear(1600))
    print(leapYear(1800))
    print(leapYear(2024))

    print(validDate(5, 24, 1962))
    print(validDate(9, 31, 2000))
    print(validDate(2, 28, 1600))
    print(validDate(2, 29, 2024))

    print(calDayNum(2, 29, 2024))
    print(calDayNum(2, 29, 1893))
    print(calDayNum(3, 25, 2024))
    print(calDayNum(3, 25, 2023))

def leapYear(year):
    """
    This function determines whether a year is a leap year and returns the boolean
    """
    if year % 100 == 0:
        if year % 400 != 0:
            return False
        else:
            return True
    elif year % 4 != 0:
        return False
    else:
        return True

def validDate(month, date, year):
    """
    This function determines a valid date within the calendar and returns it
    """
    if leapYear(year) and month == 2:
        if date >= 1 and date <= 29:
            return True
        else:
            return False
    elif month == 2:
        if date >= 1 and date <= 28:
            return True
        else:
            return False
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if date >= 1 and date <= 30:
            return True
        else:
            return False
    elif month >= 1 and month <= 12:
        if date >= 1 and date <= 31:
            return True
        else:
            return False

def calDayNum(month, date, year):
    """
    This function find the day of the year and returns the number
    """
    if not validDate(month, date, year):
        return -1
    else:
        day_num = 31 * (month - 1) + date
        if month > 2:
            day_num -= (4 * month + 23) // 10
        if leapYear(year) and month > 2:
            day_num += 1
        return day_num

main()
