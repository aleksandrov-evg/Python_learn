a = list(map(int, input().split()))
prevNum = 0
countInt = 0
for i in a:
    if prevNum != i:
        countInt += 1
        prevNum = i
if len(a) == 1:
    countInt = 1
print(countInt)
