for i in range(10, 100):
    a = [int(i) for i in str(i)]
    if (a[0] * a[1]) * 2 == i:
        print(i)
