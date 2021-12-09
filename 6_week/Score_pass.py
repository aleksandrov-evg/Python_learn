inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
gradeList = []
k = int(inFile.readline())
for line in inFile.readlines():
    line.rstrip('\n')
    a = list(map(lambda x: int(x), line.rsplit(' ', 3)[1:]))
    if a[0] >= 40 and a[1] >= 40 and a[2] >= 40:
        gradeList.append(sum(a))
inFile.close()
gradeList.sort(reverse=True)
if len(gradeList) <= k:
    print(0, file=outFile)
else:
    if gradeList[0] == gradeList[k]:
        print(1, file=outFile)
    else:
        while gradeList[k] == gradeList[k - 1]:
            k -= 1
        print(gradeList[k-1], file=outFile)
