i = int(input())
forTransform = i
countPalindrom = 0
while i >= 1:
    revNumber = 0
    while forTransform > 0:
        currentDigit = forTransform % 10
        forTransform //= 10
        revNumber *= 10
        revNumber += currentDigit
    if revNumber == i:
        countPalindrom += 1
    i -= 1
    forTransform = i
print(countPalindrom)
