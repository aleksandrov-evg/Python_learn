def ReduceFraction(n, m):
    a, b = n, m
    if b > a:
        a, b = m, n
    return n // gcd(a, b), m // gcd(a, b)


def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


n, m = int(input()), int(input())
print(*ReduceFraction(n, m))
