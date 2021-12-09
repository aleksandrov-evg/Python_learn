fin = open('input.txt')
wordDict = {}
curMax = ['', 0]
for line in fin.readlines():
    line = line.strip('\n').split()
    for word in line:
        wordDict[word] = wordDict.get(word, 0) + 1
        if curMax[1] < wordDict[word]:
            curMax[0] = word
            curMax[1] = wordDict[word]
        elif curMax[1] == wordDict[word] and curMax[0] > word:
            curMax[0] = word
print(curMax[0])
