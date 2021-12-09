fin = open('input.txt')
wordsDict = {}
for line in fin.readlines():
    line = line.strip('\n').split()
    for word in line:
        wordsDict[word] = wordsDict.get(word, 0) + 1
wordList = [(wordsDict[i], i) for i in wordsDict]
wordList.sort(key=lambda x: (-x[0], x[1]))
print(*[i[1] for i in wordList], sep='\n')
