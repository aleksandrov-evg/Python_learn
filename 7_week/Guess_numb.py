countNum = int(input())
yesSet = {i + 1 for i in range(countNum)}
a = None
while a != 'HELP':
    tempSet = tuple(map(str, input().split()))
    if tempSet[0] == 'HELP':
        a = 'HELP'
    else:
        a = input()
    if a == 'NO':
        yesSet -= set(map(int, tempSet))
    elif a == 'YES':
        yesSet &= set(map(int, tempSet))
print(*sorted(yesSet))
