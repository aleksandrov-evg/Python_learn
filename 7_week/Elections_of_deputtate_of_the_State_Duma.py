fin = open('input.txt')
vDict = {}
summVote = 0
for line in fin.readlines():
    line = line.strip('\n').rsplit(' ', 1)
    vDict[line[0]] = vDict.get(line[0], [0]) + [int(line[1])]
    summVote += vDict[line[0]][1]
fElQue = summVote / 450
sumFirstRound = 0
fin.close()
for p in vDict:
    vDict[p][0] = vDict[p][1] // fElQue
    sumFirstRound += vDict[p][0]
    vDict[p] += [(vDict[p][1] / fElQue) - (vDict[p][1] // fElQue)]
while sumFirstRound < 450:
    for x in sorted(vDict, key=lambda i: (-vDict[i][2], vDict[i][1])):
        vDict[x][0] += 1
        sumFirstRound += 1
        if sumFirstRound == 450:
            break
print(*[x + ' ' + str(int(vDict[x][0])) for x in vDict], sep='\n')
