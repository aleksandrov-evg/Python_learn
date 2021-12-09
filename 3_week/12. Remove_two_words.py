a = str(input())
print(a[a.find(' ') + 1:] + ' ' + a[:a.find(' ')])
