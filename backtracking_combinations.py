animals = ['cat', 'dog', 'monkey', 'lion', 'zebra', 'giraffe']
#animals = ['cat', 'monkey', 'dog']
COUNT = 2
# all combinations of animals of size 2.

n = len(animals)
a = [[],[]]
def backtrack(a,k):
    # check if the current configuration is a solution and process it.
    if k == n:
        print(a)
    else:
    # Extend the current partial solution to find a valid solution
        curr = animals[k]
        k += 1
        a[0].append(curr)
        # all combinations with curr in the first set.
        backtrack(a,k)
        a[0].pop()
        a[1].append(curr)
        # all combinations with curr in the second set.
        backtrack(a,k)
        a[1].pop()
    return
backtrack(a,0)

