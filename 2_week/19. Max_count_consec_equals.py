i = -1
currentNumber = -1
countRep = 1
countMaxRepeat = 1
while i != 0:
    i = int(input())
    if i != currentNumber:
        if countRep > countMaxRepeat:
            countMaxRepeat = countRep
        countRep = 1
        currentNumber = i
    elif i == currentNumber:
        countRep += 1
print(countMaxRepeat)
