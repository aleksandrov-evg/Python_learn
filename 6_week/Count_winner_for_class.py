inFile = open('input.txt', 'r', encoding='utf8')
gradeList = []
for line in inFile.readlines():
    line.rstrip('\n')
    a = line.split()[2:]
    a[0], a[1] = int(a[0]), [int(a[1])]
    if len(gradeList) == 0:
        gradeList.append(a)
    else:
        chkIns = 0
        for i in range(len(gradeList)):
            if a[0] == gradeList[i][0]:
                gradeList[i][1] += a[1]
                chkIns = 1
            if i == len(gradeList) - 1 and chkIns == 0:
                gradeList.append(a)
inFile.close()
gradeList.sort(key=lambda x: x[0])
for i in range(len(gradeList)):
    print(gradeList[i][1].count(max(gradeList[i][1])), end=' ')
