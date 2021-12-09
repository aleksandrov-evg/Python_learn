a = list(map(int, input().split()))
x1 = a.index(min(a))
x2 = a.index(max(a))
a[x2], a[x1] = a[x1], a[x2]
print(*a)
