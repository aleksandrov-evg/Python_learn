n = int(input())
result = 0
prevFact = 1
for n in range(1, n + 1):
    prevFact *= n
    result += prevFact
print(result)
