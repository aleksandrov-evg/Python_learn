n = int(input())
rate = 1
while n >= rate:
    if n == rate:
        print('YES')
        break
    rate *= 2
    if n < rate:
        print('NO')
