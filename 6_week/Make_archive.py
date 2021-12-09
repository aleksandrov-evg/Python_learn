s, n = map(int, input().split())
userSizeBckp = []
curMem, numUserBck = 0, 0
for n in range(n):
    userSizeBckp.append(int(input()))
userSizeBckp.sort()
for i in userSizeBckp:
    if curMem + i <= s:
        numUserBck += 1
        curMem += i
print(numUserBck)
