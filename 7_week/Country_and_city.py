n = int(input())
cityDict = {}
searchList = []
for _ in range(n):
    a = list(map(str, input().split()))
    cityDict[a[0]] = set(a[1:])
m = int(input())
[searchList.append(str(input())) for i in range(m)]
for x in searchList:
    for city in cityDict:
        if x in cityDict[city]:
            print(city)
