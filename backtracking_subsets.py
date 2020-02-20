import io
n = int(input())
# all subsets of {1,2,3, ... , n}

def printSubstring(arr):
    f = io.StringIO()
    f.write('{')
    # Flag to check if an extra comma is present at the end
    extraComma = False
    for elem in a:
        f.write('{},'.format(elem))
        extraComma = True

    if extraComma:
        # Pop comma after last element
        lastPos = f.tell()
        f.truncate(lastPos - 1)

    f.write('}')
    print(f.getvalue())
    return

a = []
def backtrack(a,k):
    # check if the current configuration is a solution and process it.
    if k == n:
        printSubstring(a)
    else:
    # Extend the current partial solution to find a valid solution
        k += 1
        # Enumerates all subsets where k is present
        a.append(k)
        backtrack(a,k)
        # Enumerates all subsets where k is not present
        a.pop()
        backtrack(a,k)

backtrack(a,0)

