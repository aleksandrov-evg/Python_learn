n = int(input())
mistCount = 0
distSet = {}
for d in range(n):
    wordInDict = input().strip('\n')
    if wordInDict.lower() in distSet.keys():
        distSet[wordInDict.lower()].append(wordInDict)
    else:
        distSet[wordInDict.lower()] = [wordInDict]
peteVar = input().split()
for word in peteVar:
    indUppLet = []
    for let_ind in range(len(word)):
        if word[let_ind].isupper():
            indUppLet.append(let_ind)
    if len(indUppLet) == 0:
        mistCount += 1
    elif len(indUppLet) == 1:
        if word.lower() in distSet and word not in distSet[word.lower()]:
            mistCount += 1
    elif len(indUppLet) == len(indUppLet):
            mistCount += 1
    else:
        if len(distSet) == 0 or word.lower() not in distSet:
            mistCount += 1
        elif word.lower() in distSet:
            chkIndict = 0
            for i in indUppLet:
                tmpWord = list(word.lower()[:])
                tmpWord[i] = tmpWord[i].upper()
                if ''.join(tmpWord) in distSet[word.lower()]:
                    chkIndict = 1
            if chkIndict == 0:
                mistCount += 1
print(mistCount)
