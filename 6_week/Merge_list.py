def mergeList(aList, bList):
    cList = []
    aPos = 0
    bPos = 0
    for i in range(len(aList) + len(bList)):
        if aPos < len(aList) and bPos < len(bList):
            if aList[aPos] < bList[bPos]:
                cList.append(aList[aPos])
                aPos += 1
            else:
                cList.append(bList[bPos])
                bPos += 1
        else:
            if aPos < len(aList):
                cList.extend(aList[aPos::])
            else:
                cList.extend(bList[bPos::])
            return cList


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*mergeList(a, b))
