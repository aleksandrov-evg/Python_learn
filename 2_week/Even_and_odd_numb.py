a, b, c = int(input()), int(input()), int(input())
if a // 2 == a / 2 or b // 2 == b / 2 or c // 2 == c / 2:
    if a // 2 != a / 2 or b // 2 != b / 2 or c // 2 != c / 2:
        print('YES')
    else:
        print('NO')
else:
    print('NO')

