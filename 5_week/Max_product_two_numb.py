a = list(map(int, input().split()))
product = 0
mult_1 = 0
mult_2 = 0
a.sort()
for i in range(len(a) - 1):
    if a[i] * a[i + 1] > product:
        mult_1 = a[i]
        mult_2 = a[i + 1]
        product = mult_1 * mult_2
print(mult_1, mult_2, sep=' ')
