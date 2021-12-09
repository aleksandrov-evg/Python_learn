fin = open('input.txt')
shopBase = {}
for l in fin.readlines():
    l = l.strip('\n').split()
    if shopBase.get(l[0]) is None:
        shopBase[l[0]] = {l[1]: int(l[2])}
    else:
        shopBase[l[0]][l[1]] = shopBase[l[0]].get(l[1], 0) + int(l[2])
for user in sorted(shopBase):
    print(user, end=':\n')
    for item in sorted(shopBase[user]):
        print(item, shopBase[user][item])
