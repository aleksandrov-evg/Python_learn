def power(a_, n_):
    if n_ == 0:
        return 1
    elif n_ == 1:
        return a_
    elif n_ > 1:
        return a_ * power(a_, n_ - 1)


a, n = float(input()), int(input())
print(power(a, n))
