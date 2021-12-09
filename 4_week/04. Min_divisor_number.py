def MinDivisor(n_):
    sqr = n_ ** 0.5
    dev = 2
    if n_ != 0 and n_ != 1:
        while n_ % dev != 0:
            dev += 1
            if dev > sqr:
                return n_
        return dev
    else:
        return n_


n = int(input())
print(MinDivisor(n))
