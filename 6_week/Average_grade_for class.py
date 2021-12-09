inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
averLst = []
for line in inFile.readlines():
    line.rstrip('\n')
    a = line.split()[2:]
    a[0], a[1] = int(a[0]), [int(a[1])]
    if len(averLst) == 0:
        averLst.append(a)
    else:
        for i in range(len(averLst)):
            if averLst[i][0] == a[0]:
                averLst[i][1].extend(a[1])
                break
            elif i == len(averLst) - 1:
                averLst.append(a)
averLst.sort(key=lambda x: x[0])
for i in averLst:
    print(sum(i[1]) / len(i[1]), end=' ', file=outFile)
inFile.close()
outFile.close()