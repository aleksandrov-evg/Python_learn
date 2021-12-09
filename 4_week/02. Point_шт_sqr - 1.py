def IsPointInSquare(x_, y_):
    return -1 <= x_ <= 1 and -1 <= y_ <= 1


x, y = float(input()), float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
