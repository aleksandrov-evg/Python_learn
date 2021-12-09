inFile = open('input.txt', 'r', encoding='utf8')
colAnn, colBore, switchSet = None, None, None
setAnn, setBore = set(), set()
for line in inFile.readlines():
    line = line.rstrip('\n')
    if colAnn is None and colBore is None:
        colAnn, colBore = map(int, line.split())
        switchSet = colAnn
    else:
        line = int(line)
        if switchSet >= 1:
            setAnn.add(line)
            switchSet -= 1
        else:
            setBore.add(line)
print(len(setAnn & setBore))
print(*sorted((setAnn & setBore)))
print(len(setAnn - setBore))
print(*sorted(setAnn - setBore))
print(len(setBore - setAnn))
print(*sorted(setBore - setAnn))
