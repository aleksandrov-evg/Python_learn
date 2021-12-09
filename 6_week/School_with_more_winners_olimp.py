inFile = open('input.txt', 'r', encoding='utf8')
schoolList = [0] * 100
for line in inFile.readlines():
    line.rstrip('\n')
    a = line.split()[2:3]
    schoolList[int(a[0]) - 1] += 1
for i in range(len(schoolList)):
    if schoolList[i] == max(schoolList):
        print(i + 1, end=' ')
