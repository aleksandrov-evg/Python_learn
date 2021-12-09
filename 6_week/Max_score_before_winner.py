inFile = open('input.txt', 'r', encoding='utf8')
gradeList = [[] for x in range(12)]
for line in inFile.readlines():
    line.strip('\n')
    a = line.split()[2:]
    a[0], a[1] = int(a[0]), int(a[1])
    gradeList[a[0]] += [a[1]]
for i in range(len(gradeList)):
    if len(gradeList[i]) != 0:
        gradeList[i].sort(reverse=True)
        curMax = gradeList[i][0]
        for j in gradeList[i]:
            if j != curMax:
                print(j, end=' ')
                break
