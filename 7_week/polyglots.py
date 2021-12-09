studList = []
for stud in range(int(input())):
    studList.append({input() for i in range(int(input()))})
allStudSet = studList[0]     # знают все ученики
allLangSet = set()      # языки которые знает класс
for a in studList:
    allLangSet |= a
    allStudSet &= a
print(len(allStudSet), *allStudSet, len(allLangSet), *allLangSet, sep='\n')
