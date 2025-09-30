def findIndex(list, num):
    for i in range(len(list)):
        if num < list[i]:
            return i
    return len(list)

def insertionSort(list, num):
    newList = []
    for i in range(len(list)):
        newList.insert(findIndex(list, i), len(list))
        list.remove(findIndex(list, i))
    return newList

testList = [26, 14, 8, 7, 42]

print(insertionSort(testList, 42))
