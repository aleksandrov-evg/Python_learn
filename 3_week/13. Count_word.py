a = str(input())
if a.count(' ') == 1:
    print(2)
elif a.count(' ') > 1:
    print(a.count(' ') + 1)
else:
    print(1)
