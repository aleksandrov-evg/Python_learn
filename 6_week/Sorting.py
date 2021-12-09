n = int(input())
L = list(map(int, input().split()))[:n]
print(*sorted(L))
