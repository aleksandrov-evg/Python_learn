def min4(a, b, c, d):
    return min(min(a, b), min(c, d))


x1, x2, x3, x4 = int(input()), int(input()), int(input()), int(input())
print(min4(x1, x2, x3, x4))
