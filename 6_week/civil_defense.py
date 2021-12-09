def sortBySec(InPair):
    return InPair[1]


n = int(input())
cityIn = tuple(map(int, input().split()))
m = int(input())
vaultIn = tuple(map(int, input().split()))
resultList = [None] * n
cL = [(i, cityIn[i]) for i in range(n)]
vL = [(i, vaultIn[i]) for i in range(m)]
cL.sort(key=sortBySec)
vL.sort(key=sortBySec)
vI = 0  # start index for search nearest vault
for cI in range(len(cL)):
    for vI in range(len(vL)):
        if len(vL) == 1:
            resultList[cL[cI][0]] = vL[0][0] + 1
        elif vI == len(vL) - 1:
            resultList[cL[cI][0]] = vL[vI][0] + 1
        else:
            a1 = abs(vL[vI][1] - cL[cI][1])
            a2 = abs(vL[vI + 1][1] - cL[cI][1])
            if a1 <= a2:
                resultList[cL[cI][0]] = vL[vI][0] + 1
                break
            elif a1 > a2:
                vI += 1
print(*resultList)
