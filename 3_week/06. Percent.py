p, x, y = int(input()), int(input()), int(input())
percent = int((p * ((x * 100) + y)) / 100)
result = float((x + (y / 100)) + (percent / 100))
print(int(result), round((result % 1) * 100))
