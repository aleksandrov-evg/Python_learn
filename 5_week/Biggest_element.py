a = list(map(int, input().split()))
curMax = a[0]
curMaxInd = 0
for i in range(0, len(a) - 1):
    if a[i + 1] > curMax:
        curMax = a[i + 1]
        curMaxInd = i + 1
print(curMax, curMaxInd)
