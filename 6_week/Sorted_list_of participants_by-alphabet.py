inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()
listStud = []
for line in lines:
    line = line.strip('\n')
    b = line.split()
    b = [i for i in b]
    b[2], b[3] = int(b[2]), int(b[3])
    listStud.append(b)
listStud.sort(key=lambda x: x[0])

for i in listStud:
    print(i[0], i[1], i[3], file=outFile)
inFile.close()
outFile.close()
