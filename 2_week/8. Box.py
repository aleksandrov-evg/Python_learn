a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())
if a1 > b1:
    a1, b1 = b1, a1
if b1 > c1:
    b1, c1 = c1, b1
if a1 > b1:
    a1, b1 = b1, a1
if a2 > b2:
    a2, b2 = b2, a2
if b2 > c2:
    b2, c2 = c2, b2
if a2 > b2:
    a2, b2 = b2, a2

a = a1 - a2
b = b1 - b2
c = c1 - c2

if a == b == c == 0:
    print('Boxes are equal')
elif a >= 0 and b >= 0 and c >= 0:
    print('The first box is larger than the second one')
elif a <= 0 and b <= 0 and c <= 0:
    print('The first box is smaller than the second one')
else:
    print('Boxes are incomparable')

'''
if (a1 == a2) and (b1 == b2) and (c1 == c2):
    print('Boxes are equal')
elif a1 >= a2 and c1 <= c2:
    print('The first box is larger than the second one')
elif a2 >= a1 and c2 >= c1:
    print('The first box is smaller than the second one')
else:
    print('Boxes are incomparable')
'''

# print('Range SECOND', a2, b2, c2)
# print('Range FIRST', a1, b1, c1)
