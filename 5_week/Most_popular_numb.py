a = list(map(int, input().split()))
maxInc = 0
curMax = 0
for i in a:
    if a.count(i) > maxInc:
        maxInc = a.count(i)
        curMax = i
print(curMax)
