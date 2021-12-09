n = 0
mySet = set()
for i in map(int, input().split()):
    n = len(mySet)
    mySet.add(i)
    if n != len(mySet):
        print('NO')
    else:
        print('YES')
