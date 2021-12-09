fin = open('input.txt')
words = {}
for line in fin.readlines():
    for word in line.strip().split():
        words[word] = words.get(word, 0) + 1
        print(words[word] - 1, end=' ')
