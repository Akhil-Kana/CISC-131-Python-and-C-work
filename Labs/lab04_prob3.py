"""
CISC 131 Problem 3 - Akhil Kanayinkal (kana9520) and Nathan Kostynick (kost6288)
"""

def naturalLog(z, num_terms):
    """
    This function finds the natural log of a number
    """

    value = 3
    answer = (z-1)/(z+1)
    for _i in range(1, num_terms):
        answer += ((1/value)*((z-1)/(z+1))**value)
        value +=2
    answer *= 2
    return answer

print(naturalLog(3, 100))
