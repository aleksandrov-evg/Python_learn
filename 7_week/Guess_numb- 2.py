maxNum = int(input())
a = None
yesSet = {i + 1 for i in range(maxNum)}
answerList = []
while a != 'HELP':
    tempSet = tuple(map(str, input().split()))
    if tempSet[0] == 'HELP':
        a = 'HELP'
        tempSet = ()
        print(*answerList, sep='\n')
        print(*sorted(yesSet))
    else:
        tempSet = set(map(int, tempSet))
        tempSet &= yesSet
        if 1 < len(tempSet) > len(yesSet) / 2:
            answerList.append('YES')
            yesSet &= tempSet
        elif 1 < len(tempSet) <= len(yesSet) / 2:
            answerList.append('NO')
            yesSet -= tempSet
        elif len(tempSet) == 1:
            if len(tempSet) == len(yesSet) == 1:
                answerList.append('YES')
            answerList.append('NO')
            yesSet -= tempSet
