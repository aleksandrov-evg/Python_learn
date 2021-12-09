fin = open('input.txt')
voteDict = {}
for line in fin.readlines():
    line = line.strip('\n').split()
    voteDict[line[0]] = voteDict.get(line[0], 0) + int(line[1])
print(*sorted([i + ' ' + str(voteDict[i]) for i in voteDict]), sep='\n')



