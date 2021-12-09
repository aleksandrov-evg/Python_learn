a = list(map(int, input().split()))
i = len(a) if len(a) % 2 == 0 else len(a) - 1
curStep = 0
while i >= 2:
    a[curStep], a[curStep + 1] = a[curStep + 1], a[curStep]
    curStep += 2
    i -= 2
print(*a)
