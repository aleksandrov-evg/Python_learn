def CountSort(A):
    sortList = [0] * 101
    newList = []
    for aF in A:
        sortList[aF] += 1
    for bF in range(len(sortList)):
        while sortList[bF] > 0:
            newList.append(bF)
            sortList[bF] -= 1
    return newList

a = list(map(int, input().split()))
print(*CountSort(a))
