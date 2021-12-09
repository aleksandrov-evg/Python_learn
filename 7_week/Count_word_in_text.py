#inFile = open('input.txt', 'r', encoding='utf8')
word = set()
for line in inFile.readlines():
    word |= set(line.strip('\n').split())
print(len(word))
