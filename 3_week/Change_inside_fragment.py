a = str(input())
posFirstH = a.find('h')
posLastH = a.rfind('h')
b = a[posFirstH + 1:posLastH]
print(a[:posFirstH + 1] + b.replace('h', 'H') + a[posLastH:])
