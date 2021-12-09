fin = open('input.txt', encoding='utf8')
fOut = open('output.txt', 'w', encoding='utf8')
voteBase = {}
countVote = int()
for candName in fin.readlines():
    candName = candName.strip('\n')
    countVote += 1
    voteBase[candName] = voteBase.get(candName, 0) + 1
resVote = []
[resVote.append((i, voteBase[i])) for i in voteBase]
resVote.sort(key=lambda x: -x[1])
if countVote / 2 < resVote[0][1]:
    print(resVote[0][0], file=fOut)
else:
    print(resVote[0][0], resVote[1][0], sep='\n', file=fOut)


outFile = open("output.txt", "w", encoding='utf-8')
fin = open('input.txt', 'r', encoding='utf-8')
people = dict()
count = 0
for line in fin:
    people[line.strip()] = people.get(line.strip(), 0) + 1
    count += 1
p = sorted(people, key=lambda x: (-people[x], x))
if people[p[0]] > count / 2:
    print(p[0], file=outFile)
else:
    print(p[0], p[1], sep='\n', file=outFile)
outFile.close()
fin.close()