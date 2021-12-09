numDay, numbParty = map(int, input().split())
holidaySet = set()
for i in range(6, numDay + 1, 7):
    holidaySet.add(i)
    holidaySet.add(i + 1)
strikeDay = set()
for i in range(numbParty):
    startDay, pause = map(int, input().split())
    curDate = 0
    tempSet = {x for x in range(startDay, numDay + 1, pause)}
    strikeDay |= tempSet
strikeDay -= holidaySet
print(len(strikeDay))
