a = list(map(int, input().split()))
k = int(input())
print(*a[0:k], *a[k+1:len(a)])
