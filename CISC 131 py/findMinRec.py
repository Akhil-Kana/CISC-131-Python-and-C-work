def minLst(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        if lst[0] > lst[1]:
            lst.pop(0)
        else:
            lst.pop(1)
    return minLst(lst)

print(minLst([0, 7, 8, -2, 10]))

def minLst2(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        _min = minLst2(lst[1:])
        return lst[0] if lst[0] < _min else _min

print(minLst2([0, 7, 8, -2, 10]))
