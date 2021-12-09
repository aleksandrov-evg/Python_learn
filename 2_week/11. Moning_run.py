x, y = int(input()), int(input())
currentMillage = x
countDay = 1
if currentMillage >= y:
    print(countDay)
elif currentMillage < y:
    while currentMillage - y < 0:
        countDay += 1
        currentMillage = currentMillage + (currentMillage * 0.1)
    print(countDay)
