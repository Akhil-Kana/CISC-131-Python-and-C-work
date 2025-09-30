def toLetterGrade(num):
    if num >= 90:
        return "A"
    elif num < 60:
        return "F"
    elif num >= 80:
        return "B"
    elif num >= 70:
        return "C"
    else:
        return "D"

def toLetterGrade2(num):
    if num < 60:
        return 'F'
    else:
        ten_digit = int(num/10)
        ascii_val = 74 - ten_digit
        return chr(ascii_val)

def main():
    print(toLetterGrade(92))
    print(toLetterGrade(83))
    print(toLetterGrade(59))
    print(toLetterGrade(60))
    print(toLetterGrade(72))

    print()

    print(toLetterGrade2(92))
    print(toLetterGrade2(83))
    print(toLetterGrade2(59))
    print(toLetterGrade2(60))
    print(toLetterGrade2(72))

main()
