"""
CISC 131 Problem 1 - Akhil Kanayinkal (kana9520)
"""

def listStats(numlst):
    """
    This function finds the min, max, and avg values of a list of numbers
    """
    minimum = 0.0
    maximum = 0.0
    average = 0.0
    numlst.sort()
    minimum = numlst[0]
    maximum = numlst[len(numlst)-1]
    for i in range(len(numlst)):
        average += numlst[i]
    average /= len(numlst)
    new_list = [minimum, maximum, average]
    return new_list

def printStats(numlst):
    """
    This function prints what's in the listStats function
    """
    string = "The minimum is {:.3f}, the maximum is {:.3f}, the average is {:.3f}"
    print(string.format(listStats(numlst)[0], listStats(numlst)[1], listStats(numlst)[2]))

print(listStats([1, 3, 5, -2, 10, -4]))
printStats([1, 3, 5, -2, 10, -4])
