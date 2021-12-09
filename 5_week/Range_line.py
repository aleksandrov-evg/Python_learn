dimList = list(map(int, input().split()))
x = int(input())
if len(dimList) == 1:
    if x <= dimList[0]:
        i = 1
    else:
        i = 0
else:
    i = 0
    dimList.append(0)
    while dimList[i] >= x:
        i += 1
print(i + 1)
