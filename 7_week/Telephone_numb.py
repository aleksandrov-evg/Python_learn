def clearNum(line_func):
    code, number = '', ''
    if line_func[0] == '8':
        line_func = line_func[1:len(line_func)]
    elif line_func[0:2] == '+7':
        line_func = line_func[2:len(line_func)]
    else:
        code = '495'
    for iF in line_func:
        if iF.isdigit():
            if len(code) < 3:
                code += iF
            else:
                number += iF
    return code + number


fin = open('input.txt')
phoneBook = set()
addNumber = clearNum(fin.readline())
for line in fin.readlines():
    if addNumber == clearNum(line):
        print('YES')
    else:
        print('NO')
