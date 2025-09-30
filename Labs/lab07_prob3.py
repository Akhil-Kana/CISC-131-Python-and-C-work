"""
CISC 131 Problem 3 - Akhil Kanayinkal (kana9520)
"""

def hasDuplicates(lst):
    """
    This function finds if there are duplicates within a list
    """
    for i in range(len(lst)):
        if lst.count(lst[i]) > 1:
            return True
    return False

def removeDuplicates(lst):
    """
    This function removes duplicates within a duplicate/new list
    """
    new_lst = lst[:]
    for i in lst:
        for _j in new_lst:
            if new_lst.count(i) > 1:
                new_lst.remove(i)
    return new_lst

def removeDuplicatesInPlace(lst):
    """
    This function removes duplicates within the same list
    """
    new_lst = lst[:]
    for i in lst:
        for _j in new_lst:
            if lst.count(i) > 1:
                lst.remove(i)

mylist = [1, 2, 3, 314, 4, 5, 6, 314]
print(hasDuplicates(mylist))
print(removeDuplicates(mylist))
print(mylist)
removeDuplicatesInPlace(mylist)
print(mylist)

print()

mylist2 = [5, 2, 2, 2, 3, 5, 5, 3]
print(hasDuplicates(mylist2))
print(removeDuplicates(mylist2))
print(mylist2)
removeDuplicatesInPlace(mylist2)
print(mylist2)
