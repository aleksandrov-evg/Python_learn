a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if d >= a and (e >= b or e >= c):
    print('YES')
elif d >= b and (e >= a or e >= c):
    print('YES')
elif d >= c and (e >= b or e >= a):
    print('YES')
else:
    print('NO')
