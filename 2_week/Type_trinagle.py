a, b, c = int(input()), int(input()), int(input())
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
'''if a + b <= c or a + c <= b or b + c <= a\
        or a <= 0 or b <= 0 or c <= 0:'''
if (a + b) > c and (c + a) > b and (c + b) > a:
    if (c ** 2) == (a ** 2 + b ** 2):
        print('rectangular')
    if (c ** 2) < (a ** 2 + b ** 2):
        print('acute')
    if (c ** 2) > (a ** 2 + b ** 2):
        print('obtuse')
else:
    print('impossible')
