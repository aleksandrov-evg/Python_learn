x = int(input())
dem = 2
if x % dem == 0:
    print(dem)
else:
    while x % dem != 0:
        dem = dem + 1
        if x % dem == 0:
            print(dem)
