def dataRecog(a):
    a.strip('\n')
    newList = list(map(int, a.split()))
    return newList


inFile = open('input.txt', 'r', encoding='utf8')
distHome = dataRecog(inFile.readline())
distHome.sort()
priceKm = dataRecog(inFile.readline())
priceKm.sort(reverse=True)
totalMinPrice = 0
for i in range(len(priceKm)):
    totalMinPrice += distHome[i] * priceKm[i]
print(totalMinPrice)
