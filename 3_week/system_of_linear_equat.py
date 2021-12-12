a, b, c, d, e, f = map(float, [input() for _ in range(6)])
x = (e * d - b * f) / (a * d - b * c)
y = (a * f - c * e) / (a * d - b * c)
print(x, y)
