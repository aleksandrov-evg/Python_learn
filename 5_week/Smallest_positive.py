a = list(map(int, input().split()))
curMin = max(a[:]) * 2
for i in a:
    if i <= curMin and i % 2 != 0:
        curMin = i
print() if curMin == max(a[:]) * 2 else print(curMin)
