a = str(input())
if a.find('f') == -1:
    print('-2')
else:
    posFirstF = a.find('f') + 1
    strAfterFirstF = a[posFirstF:]
    if strAfterFirstF.find('f') == -1:
        print(-1)
    else:
        print(strAfterFirstF.find('f') + posFirstF)
print()
