a = []
for i in range(8):
    b = list(map(int, input().split()))
    a.append(b)
availStep = a[:]
for i in range(len(a)):
    x, y = a[i][0], a[i][1]
    v = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 0]]
    for j in range(len(v)):
        x, y = a[i][0], a[i][1]
        x_step, y_step = v[j][0], v[j][1]
        while 2 <= x <= 7 and 2 <= y <= 7:
            x += x_step
            y += y_step
            availStep.append([x, y])
result = 'NO'
for s in a:
    if availStep.count(s) > 1:
        result = 'YES'
print(result)
