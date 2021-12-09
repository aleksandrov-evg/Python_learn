a = str(input())
print(a[0:a.find('h')] + a[a.rfind('h') + 1:len(a)])
