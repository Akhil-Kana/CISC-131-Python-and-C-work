"""
def funWhile(x, y):
    total = 0
    i = x
    while i < y:
        total = total + 1
        i = i +2
    return total

a) funWhile(2,2)

0

b) funWhile(2,3)

1

c) funWhile(2,6)

2

Rewrite function:

def funFor(n):
    total = 0
    for j in range(n):
        total = total+2**j
    return total

-->

def funFor(n):
    total = 0
    j = 0
    while(j<n):
        total = total+2**j
        j += 1
    return total

or

def funFor(n):
    total = 0
    while(n>=0):
        n = n-1
        total = total+2**n
    return total


"""

def countDuplicate(lst1, lst2):
    count = 0
    if len(lst1) > len(lst2):
        for i in range(len(lst1)):
            if lst1[i] == 