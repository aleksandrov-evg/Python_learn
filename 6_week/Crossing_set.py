def Intersection(A, B):
    c = []
    curChk = None
    posA = 0
    posB = 0
    for i in range(len(A) + len(B)):
        if posA < len(A) and posB < len(B):
            if A[posA] == B[posB] != curChk:
                c.append(a[posA])
                curChk = a[posA]
                posA += 1
                posB += 1
            elif A[posA] < B[posB]:
                posA += 1
            elif A[posA] > B[posB]:
                posB += 1
    return c


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*Intersection(a, b))
