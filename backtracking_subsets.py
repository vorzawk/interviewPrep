# all subsets of {1,2,3}
n = 3

a = []
def backtrack(a,k):
    if k == n:
        print(a)
    else:
        k += 1
        a.append(k)
        backtrack(a,k)
        a.pop()
        backtrack(a,k)

backtrack(a,0)

