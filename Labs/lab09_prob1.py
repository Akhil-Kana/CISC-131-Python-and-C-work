"""
CISC 131 Problem 1 - Akhil Kanayinkal (kana9520)
"""

def factors(num):
    """
    This function puts all the factors for a positive integer
    """
    lst = []
    for i in range(1, num + 1):
        if num % i == 0:
            lst.append(i)
    return lst

def exists(val, lst):
    """
    This function finds a target num within a list and determines if it exists
    """
    for i in range(len(lst)):
        if val == lst[i]:
            return True
    return False

def gcd(num1, num2):
    """
    This function finds the gcd between two numbers
    """
    num_gcd = 0
    fac1 = factors(num1)
    fac2 = factors(num2)
    if len(fac1) > len(fac2):
        for i in range(len(fac1)):
            if exists(fac1[i], fac2):
                if fac1[i] > num_gcd:
                    num_gcd = fac1[i]
    else:
        for i in range(len(fac2)):
            if exists(fac2[i], fac1):
                if fac2[i] > num_gcd:
                    num_gcd = fac2[i]
    return num_gcd

#print(factors(15))
#print(exists(3, [1, 5, 3, 9]))
#print(exists(3, [2, 0, 1, 1, 5]))
print(gcd(100250, 10000000))
print(gcd(15, 25))
