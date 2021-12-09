a, b = int(input()), int(input())
while a != b:
    if a % 2 == 0:
        if a / 2 >= b:
            print(":2")
            a = a / 2
        elif a == 2 and b == 1:
            print(":2")
            a = a / 2
        elif a - 1 >= b:
            print("-1")
            a -= 1
    else:
        if a - 1 >= b:
            print("-1")
            a -= 1
