a = str(input())
i = 0
result = ''
while i != len(a):
    result += a[i:i + 1] + '*'
    i += 1
    if i == len(a):
        result = result[:len(result) - 1]
print(result)
