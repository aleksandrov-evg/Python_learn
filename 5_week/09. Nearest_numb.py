n = int(input())
dataList = list(map(int, input().split()))
x = int(input())
tempList = []
while n > len(dataList):
    dataList.pop()
for a in dataList:
    tempList.append(abs(a - x))
print(dataList[tempList.index(min(tempList))])

