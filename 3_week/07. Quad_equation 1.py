a, b, c, = float(input()), float(input()), float(input())
D = (b ** 2) - (4 * a * c)
if D < 0:
    print()
elif D == 0:
    print((- b) / (2 * a))
elif D > 0:
    x1 = (- b + D ** 0.5) / (2 * a)
    x2 = (- b - D ** 0.5) / (2 * a)
    print(min(x1, x2), max(x1, x2))
