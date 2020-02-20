n = int(input())
# all permutations of {1,2,3, ... , n}

a = []
def backtrack(a,k):
    # check if the current configuration is a solution and process it.
    if k == n:
        a = [i+1 for i in a]
        print(a)
    else:
    # Extend the current partial solution to find a valid solution
        k += 1
        isPresent = [False] * n
        for elem in a:
            isPresent[elem] = True
        for i in range(n):
            if not isPresent[i]:
                a.append(i)
                # all the permutations with i in the kth position
                backtrack(a,k)
                a.pop()
    return
backtrack(a,0)

