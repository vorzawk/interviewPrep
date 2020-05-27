a = list(map(int, input().split()))
n = len(a)
for i in range(n):
    minIdx = i
    for j in range(i+1, n):
        if a[j] < a[minIdx]:
            minIdx = j
    a[i], a[minIdx] = a[minIdx], a[i]
print(a)





