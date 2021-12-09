p, x, y, k = int(input()), int(input()), int(input()), int(input())
currentDeposit = (x * 100 + y)
while k >= 1:
    currentDeposit += int(currentDeposit * (p / 100))
    k -= 1
print(int(currentDeposit / 100), round(((currentDeposit / 100) % 1) * 100))
