n = int(input())
a = ()
for i in range(1, n + 1):
    a += (i,)
for j in a:
    for x in range(1, j + 1):
        print(x, end='')
    print()
