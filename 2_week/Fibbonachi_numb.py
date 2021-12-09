i = int(input())
a, b = 0, 1
result = -1
step = 2
if i == 0:
    result = 0
elif i == 1:
    result = 1
else:
    while a + b < i:
        if a + b == i:
            result = 2
        elif a + b < i:
            a, b = b, a + b
            step += 1
            result = step
        if a + b > i:
            result = -1
print(result)
