def binarySearch(data, elem):
    """ Function returns the index of the element if it exists in the array or the index at which it would have been present if it is not. 
    The function expects the argument data to be in sorted order """
    low = 0
    high = len(data) - 1
    while low <= high:
        middle = (low + high) // 2
        if elem == data[middle]:
            return middle
        if elem > data[middle]:
            low = middle + 1
        else:
            high = middle - 1
    return middle

sortedList = [1, 12, 40, 41, 50, 55, 60, 75, 100]
print(sortedList)
print(binarySearch(sortedList, 75))
print(binarySearch(sortedList, 100))

