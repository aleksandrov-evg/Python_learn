testList = input().split()
countPos = 0
for i in testList:
    if int(i) > 0:
        countPos += 1
print(countPos)
