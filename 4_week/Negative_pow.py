def power(a_, n_):
    if n_ == 0:
        return 1
    if n_ > 0:
        result = a_
        n_ -= 1
        while n_ > 0:
            result *= a_
            n_ -= 1
        return result
    if n_ < 0:
        result = 1 / a_
        n_ += 1
        while n_ < 0:
            result *= 1/a_
            n_ += 1
        return result


a, n = float(input()), int(input())
print(power(a, n))
