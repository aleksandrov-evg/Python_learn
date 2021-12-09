def xor(x_, y_):
    return y_ != x_ == 1 or x_ != y_ == 1


x, y, = int(input()), int(input())
if xor(x, y):
    print(1)
else:
    print(0)
