def IsPointInCircle(x_, y_, xc_, yc_, r_):
    return ((xc_ - x_) ** 2) + ((yc_ - y_) ** 2) <= r_ ** 2


x, y, = float(input()), float(input()),
xc, yc, = float(input()), float(input()),
r = float(input())
if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print("NO")
