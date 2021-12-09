def sum_(a_, b_):
    if b_ > 0:
        a_ += 1
        b_ -= 1
        if b_ == 0:
            return a_
        else:
            return sum_(a_ + 1, b_ - 1)
    elif b_ == 0:
        return a_


a, b = int(input()), int(input())
print(sum_(a, b))
