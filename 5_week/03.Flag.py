n = int(input())
for i in range(10):
    if i == n:
        print('+___ ' * n)
for j in range(n):
    print('|', j + 1, ' / ', sep='', end='')
print()
print('|__\ ' * n, sep='')
print('|    ' * n)
