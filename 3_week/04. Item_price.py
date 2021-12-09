price = float(input())
rub = int(price)
kop = round((price % 1) * 100)
print(rub, kop)
