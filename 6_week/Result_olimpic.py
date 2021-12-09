n = int(input())
gradeList = [] * n
for i in range(n):
    a = list(map(str, input().split()))
    a[1] = int(a[1])
    gradeList.append(a)
gradeList.sort(key=lambda x: x[1], reverse=True)
for i in range(len(gradeList)):
    print(gradeList[i][0])
