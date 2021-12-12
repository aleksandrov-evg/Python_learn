a = list(map(int, input().split()))
curMax = a[len(a) - 1]
curMaxInd = len(a) - 1
for i in range(len(a) - 1, 0, -1):
    if curMax < a[i - 1]:
        curMax = a[i - 1]
        curMaxInd = i - 1
print(curMax, curMaxInd, sep=' ')
