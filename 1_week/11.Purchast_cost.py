A = int(input())
B = int(input())
N = int(input())
fullPrice = ((A * 100) + B) * N
print(fullPrice // 100, fullPrice % 100)
