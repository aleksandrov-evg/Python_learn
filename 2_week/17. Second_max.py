i = int(input())
prevMax = 0
currMax = i
while i != 0:
    i = int(input())
    if prevMax < i < currMax:
        prevMax = i
    elif i > currMax:
        prevMax = currMax
        currMax = i
    elif i == currMax:
        prevMax = currMax
print(prevMax)
