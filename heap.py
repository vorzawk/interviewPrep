# assumes that keys are unique
def heap_fix(array, i):
    # Key assumption: Both the left and and right subtrees are valid heaps
    l = 2 * i + 1
    r = 2 * i + 2
    if l >= len(array):
        return
    maxChild = l
    if r < len(array) and array[r] > array[l]:
        maxChild = r
    if array[i] > array[maxChild]:
        return
    array[i], array[maxChild] = array[maxChild], array[i]
    heap_fix(array, maxChild)

def heapify(array):
    n = len(array)
    for i in range(n // 2, -1, -1):
        heap_fix(array, i)

def heappush(array, newElem):
    array.append(newElem)
    i = len(array) - 1
    while i > 0:
        p = (i - 1) // 2
        if array[p] > array[i]:
            return
        array[i], array[p] = array[p], array[i]
        i = p

def heappop(array):
    array[0], array[-1] = array[-1], array[0]
    mxVal = array.pop()
    heap_fix(array, 0)
    return mxVal

#array = [2, 3, 4, 10, 8]
array = [9, 5, 8, 4, 3, 2, 6, 1]
heapify(array)
print(array)
heappush(array, 5)
print(array)
heappop(array)
print(array)
