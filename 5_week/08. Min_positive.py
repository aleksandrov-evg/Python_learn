a = list(map(int, input().split()))
curMin = 1000
for i in a:
    if 0 < i < curMin:
        curMin = i
print(curMin) if curMin != 1000 else print()
