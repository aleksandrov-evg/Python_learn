def dist(x1_, y1_, x2_, y2_):
    return (((x2_ - x1_) ** 2) + ((y2_ - y1_) ** 2)) ** 0.5


x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())
x3, y3 = int(input()), int(input())
print(dist(x1, y1, x2, y2) + dist(x2, y2, x3, y3) + dist(x3, y3, x1, y1))
