i = currentMax = -1
countMax = 1
while i != 0:
    i = int(input())
    if i > currentMax:
        currentMax = i
        countMax = 1
    elif i == currentMax:
        countMax += 1
if currentMax == 0:
    countMax = 0
print(countMax)
