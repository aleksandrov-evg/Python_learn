a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
result = 0
for x in range(0, 1001):
    if x - e != 0:
        chk1 = (a * x ** 3 + b * x ** 2 + c * x + d)
        chk2 = x - e
        if chk1 / chk2 == 0:
            result += 1
print(result)
