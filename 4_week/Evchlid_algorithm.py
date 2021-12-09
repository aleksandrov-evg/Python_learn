def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


a, b = int(input()), int(input())
if b > a:
    a, b = b, a
print(gcd(a, b))
