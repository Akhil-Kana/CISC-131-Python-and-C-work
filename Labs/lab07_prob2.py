"""
CISC 131 Problem 2 - Akhil Kanayinkal (kana9520)
"""

def toLetterGrade(num):
    """
    This function converts a number into a letter grade
    """
    if num < 60:
        return 'F'
    else:
        ten_digit = int(num/10)
        ascii_val = 74 - ten_digit
        return chr(ascii_val)

def countScoresInRange(scorelst, low, high):
    """
    This function finds the amount of scores that are between the limits
    """
    count = 0
    for i in range(len(scorelst)):
        if scorelst[i] >= low and scorelst[i] < high:
            count += 1
    return count

def scoresToGrades(scorelst):
    """
    This function converts scores to grades within a list
    """
    new_score_lst = []
    for i in range(len(scorelst)):
        new_score_lst.append(toLetterGrade(scorelst[i]))
    return new_score_lst

def printGradeGraph(scorelst):
    """
    This function prints a histogram of different letter grades
    """
    a_count = scoresToGrades(scorelst).count("A")
    b_count = scoresToGrades(scorelst).count("B")
    c_count = scoresToGrades(scorelst).count("C")
    d_count = scoresToGrades(scorelst).count("D")
    f_count = scoresToGrades(scorelst).count("F")
    print("A: {}".format("*" * a_count))
    print("B: {}".format("*" * b_count))
    print("C: {}".format("*" * c_count))
    print("D: {}".format("*" * d_count))
    print("F: {}".format("*" * f_count))

print(countScoresInRange([75, 82, 85, 92, 84], 80, 90))
print(scoresToGrades([85, 82, 98, 40, 68, 72, 99]))
printGradeGraph([85, 82, 90, 99, 83, 67, 25, 33])
