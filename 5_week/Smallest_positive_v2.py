a = list(map(int, input().split()))
b = ()
for i in a:
    if i % 2 != 0:
        b += (i, )
print(min(b) if len(b) != 0 else 0)
