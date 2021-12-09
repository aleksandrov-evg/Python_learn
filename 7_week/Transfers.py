a = list(map(int, input().split()))
route_1 = a[:2]
route_2 = a[2:]
route_1.sort()
route_2.sort()
firstRout = {i for i in range(route_1[0], route_1[1] + 1)}
secondRout = {i for i in range(route_2[0], route_2[1] + 1)}
print(len(firstRout & secondRout))
