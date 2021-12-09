n = int(input())
ci = list(map(int, input().split()))
k = int(input())
pj = list(map(int, input().split()))
keyList = [0] * n
for i in range(0, n):
    keyList[i] = [ci[i], []]
for j in range(k):
    keyList[pj[j] - 1][1] += [1]
for i in range(n):
    if keyList[i][0] >= sum(keyList[i][1]):
        print('NO')
    else:
        print('YES')
