n = int(input())
result = 0
while n > 0:
    result += 1/(n ** 2)
    n -= 1
resultInt = int(result)
resultFloat5 = float('{0:.6f}'.format(result))
if resultInt == result:
    print(resultInt)
elif result != resultFloat5:
    print('{0:.5f}'.format(result))
else:
    print(result)
