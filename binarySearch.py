def binarySearch(sortedList, elem):
    l = 0
    r = len(sortedList) - 1
    while l <= r:
        m = (l+r) // 2
        if elem == sortedList[m]:
            return m
        if elem > sortedList[m]:
            l = m+1
        else:
            r = m-1
    return -1
