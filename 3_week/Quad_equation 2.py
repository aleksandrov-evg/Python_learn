a, b, c, = float(input()), float(input()), float(input())
D = (b ** 2) - (4 * a * c)
if a == 0:
    if b == 0 and c == 0:
        print(3)
    elif b != 0 and c != 0:
        print(1, -c / b)
    else:
        print(0)
elif D < 0:
    print(0)
elif D == 0:
    print("1", (- b) / (2 * a))
elif D > 0:
    x1 = (- b + D ** 0.5) / (2 * a)
    x2 = (- b - D ** 0.5) / (2 * a)
    print("2", min(x1, x2), max(x1, x2))
