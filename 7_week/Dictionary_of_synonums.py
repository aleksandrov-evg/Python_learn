synDict = {}
for _ in range(int(input())):
    word = tuple(map(str, input().split()))
    synDict[word[1]] = word[0]
    synDict[word[0]] = word[1]
print(synDict[str(input())])
