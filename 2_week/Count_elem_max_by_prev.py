i = int(input())
exitResult = 0
prevI = i
while i != 0:
    prevI = i
    i = int(input())
    if i > prevI:
        exitResult += 1
print(exitResult)
