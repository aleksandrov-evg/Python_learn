def MinDivisor(n_):
    sqr = n_ ** 0.5
    dev = 2
    if n > 1:
        while n_ % dev != 0 and dev < sqr:
            dev += 1
        if dev > sqr:
            dev = n_
    else:
        dev = n_
    return dev == n_


n = int(input())
if MinDivisor(n):
    print('YES')
else:
    print('NO')
