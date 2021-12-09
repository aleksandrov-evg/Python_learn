a = list(map(int, input().split()))
b = [0 for i in range(len(a))]
pos = 0
for i in a:
    if i > 0:
        b[pos] = i
        pos += 1
a = b[:]
print(*a)
