def sumFunc():
    i = int(input())
    if i == 0:
        print(i)
        return i
    else:
        sumFunc()
    return print(i)


sumFunc()
