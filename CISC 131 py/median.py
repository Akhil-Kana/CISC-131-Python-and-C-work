import math

def findMedian(lst):
    median = 0.0
    new_lst = lst[:]
    new_lst.sort()
    if len(new_lst)%2 == 1:
        median = new_lst[math.floor(len(new_lst)/2)]
    elif len(new_lst) % 2 == 0:
        num1 = new_lst[len(new_lst)//2-1]
        num2 = new_lst[len(new_lst)//2]
        median = (num1 + num2)/2
    return median

print(findMedian([5,2,3,6,1]))
print(findMedian([5,2,3,6,1,7]))
