footSize = int(input())
shoeSize = list(map(int, input().split()))
availList = []
shoeSize.sort()
stepFindPair = 0
for i in shoeSize:
    if footSize <= i and len(availList) == 0:
        availList.append(i)
    if len(availList) > 0:
        if availList[len(availList)-1] + 3 <= i:
            availList.append(i)
print(len(availList))
