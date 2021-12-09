a = list(map(int, input().split()))
max1 = a.pop(a.index(max(a)))
max2 = a.pop(a.index(max(a)))
max3 = max(a)

a.append(max1)
a.append(max2)

min1 = a.pop(a.index(min(a)))
min2 = min(a)

a.append(min1)

if max1 * max2 * max3 > max1 * min1 * min2:
    print(max1, max2, max3)
else:
    print(max1, min1, min2)
