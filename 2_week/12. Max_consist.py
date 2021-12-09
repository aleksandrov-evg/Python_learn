currInput = int(input())
if currInput != 0:
    currMax = currInput
    while currInput != 0:
        currInput = int(input())
        if currInput > currMax:
            currMax = currInput
    print(currMax)
