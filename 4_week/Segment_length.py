def distance(x1, y1, x2, y2):
    return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5


x1_, y1_ = float(input()), float(input())
x2_, y2_ = float(input()), float(input())
print(distance(x1_, y1_, x2_, y2_))
