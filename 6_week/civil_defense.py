def second(q):
    return q[1]


def first(q):
    return q[0]


numb_city = int(input())
a = list(map(int, input().split()))
a1 = []
for i in range(numb_city):
    a1.append([i, a[i], 0])
a1.sort(key=second)
mbomb = int(input())
b = list(map(int, input().split()))
b1 = []
for i in range(mbomb):
    b1.append([i, b[i]])
b1.sort(key=second)
j = 0
for i in range(0, numb_city):
    dist = abs(a1[i][1] - b1[j][1])
    while j < len(b1)-1 and \
            dist > abs(a1[i][1] - b1[j + 1][1]):
        j += 1
        dist = abs(a1[i][1] - b1[j][1])
    else:
        a1[i][2] = b1[j][0] + 1

a1.sort(key=first)
i = 0
for i in range(0, numb_city):
    print(a1[i][2], end=' ')
