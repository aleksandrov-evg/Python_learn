a = str(input())
beforeFirstH = a[0:a.find('h') + 1]
afterLastH = a[a.rfind('h'):len(a)]
betweenH = a[a.find('h') + 1:a.rfind('h')]
print(beforeFirstH + betweenH + betweenH + afterLastH)
