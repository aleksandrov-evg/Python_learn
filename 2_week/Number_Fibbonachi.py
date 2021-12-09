i = int(input())
currentValue, step = 0, 0
if i == 1:
    currentValue = 1
elif i > 1:
    prevValue = 0
    prevPrevValue = 1
    while step != i:
        currentValue = prevValue + prevPrevValue
        prevPrevValue = prevValue
        prevValue = currentValue
        step += 1
print(currentValue)
