n = int(input())
rate = 1
print(1, end=' ')
while n >= 2 ** rate:
    print(2 ** rate, end=' ')
    rate += 1
