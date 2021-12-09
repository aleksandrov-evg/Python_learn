N, k = map(int, input().split())
a = ['I' for i in range(N)]
for i in range(k):
    x, y = map(int, input().split())
    for j in range(x - 1, y):
        a[j] = '.'
print(*a, sep='')
