a = str(input())
i = 0
result = ''
startOfRang = 1
endOfRange = 3
while i != len(a):
    i += 1
    if i != 1 or (i - 1) % 3 != 0:
        result += a[startOfRang:endOfRange]
        startOfRang += 3
        endOfRange += 3
print(result)
