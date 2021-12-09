def IsAscending(A):
    step = 0
    result = 1
    while result > 0 and step < len(A) - 1:
        result = 0
        result = A[step + 1] - A[step]
        step += 1
    return result


a = list(map(int, input().split()))
if IsAscending(a) > 0:
    print('YES')
else:
    print('NO')
