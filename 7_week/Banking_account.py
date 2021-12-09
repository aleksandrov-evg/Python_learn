fin = open('input.txt')
clientBase = {}
for com in fin.readlines():
    com = com.strip('\n').split()
    if com[0] == 'DEPOSIT':
        clientBase[com[1]] = clientBase.get(com[1], 0) + int(com[2])
    elif com[0] == 'WITHDRAW':
        clientBase[com[1]] = clientBase.get(com[1], 0) - int(com[2])
    elif com[0] == 'BALANCE':
        if com[1] in clientBase.keys():
            print(clientBase[com[1]])
        else:
            print('ERROR')
    elif com[0] == 'TRANSFER':
        clientBase[com[2]] = clientBase.get(com[2], 0) + int(com[3])
        clientBase[com[1]] = clientBase.get(com[1], 0) - int(com[3])
    elif com[0] == 'INCOME':
        for user in clientBase:
            if clientBase[user] > 0:
                clientBase[user] *= 1 + int(com[1]) / 100
                clientBase[user] = int(clientBase[user])
