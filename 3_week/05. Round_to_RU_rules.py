i = float(input())
whole = int(i)
if i >= 0:
    dec = (i % 1) * 100
    if dec >= 50:
        print(int(i) + 1)
    else:
        print(int(i))
else:
    dec = (-i % 1) * 100
    if dec >= 50:
        print(int(i) - 1)
    else:
        print(int(i))
