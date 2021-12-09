a = list(map(int, input().split()))
temp = a[0]
i = 1
while i < len(a):
    a[i], temp = temp, a[i]
    i += 1
a[0] = temp
print(*a)
