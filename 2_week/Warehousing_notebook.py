a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())

# сравнение 1
if a1 > b1:
    a1, b1 = b1, a1
if b1 > c1:
    b1, c1 = c1, b1
if a1 > b1:
    a1, b1 = b1, a1

# сравнение 2
if a2 > b2:
    a2, b2 = b2, a2
if b2 > c2:
    b2, c2 = c2, b2
if a2 > b2:
    a2, b2 = b2, a2

maxCapacity = max(
    (a1 // a2) * (b1 // b2) * (c1 // c2),
    (a1 // b2) * (b1 // a2) * (c1 // c2),
    (a1 // a2) * (b1 // c2) * (c1 // b2),
    (a1 // b2) * (b1 // c2) * (c1 // a2),
    (a1 // c2) * (b1 // b2) * (c1 // a2),
    (a1 // c2) * (b1 // a2) * (c1 // b2),
)
print(maxCapacity)
