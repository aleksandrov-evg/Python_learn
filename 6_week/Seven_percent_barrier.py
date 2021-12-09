inFile = open('input.txt', 'r', encoding='utf8')
modeRead = 0    # : 0- дефолт, 1 - ввод списка партий, 2 - голосование
voteList = []
numVote = 0
for line in inFile.readlines():
    line = line.rstrip('\n')
    if line == 'PARTIES:':
        modeRead = 1
    elif line == 'VOTES:':
        modeRead = 2
    else:
        if modeRead == 1:
            voteList.append([line, 0])
        if modeRead == 2:
            for i in range(len(voteList)):
                if voteList[i][0] == line:
                    voteList[i][1] += 1
                    numVote += 1
inFile.close()
for j in voteList:
    if j[1] / numVote >= 0.07:
        print(j[0])
