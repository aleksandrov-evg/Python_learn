a, b = int(input()), int(input())
for i in range(a, b + 1):
    x = str(i)
    y = x[3:1:-1]
    if x[0:2] == y:
        print(i)
