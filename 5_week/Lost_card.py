N = int(input())
tupleCard = ()
for i in range(N - 1):
    b = int(input())
    tupleCard += (b,)
tupleCard += ('',)
for j in range(1, len(tupleCard) + 1):
    findCard = 0
    for fNum in tupleCard:
        if j == fNum:
            findCard = 1
    if findCard == 0:
        print(j)
