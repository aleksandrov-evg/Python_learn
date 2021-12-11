import copy
from sys import stdin


class Matrix:
    def __init__(self, in_list):
        self.list_in_class = copy.deepcopy(in_list)

    def __str__(self):
        self.result = ''
        for el in self.list_in_class:
            self.result += '\t'.join([str(i) for i in el]) + '\n'
        return self.result.strip('\n')

    def size(self):
        return len(self.list_in_class), len(self.list_in_class[0])

    def __add__(self, other):
        first = self.list_in_class
        second = other.list_in_class
        add_f_s = []
        for i in range(len(first)):
            add_f_s.append(
                [first[i][x] + second[i][x]
                 for x in range(len(first[i]))]
            )
        return Matrix(add_f_s)

    def __mul__(self, other):
        mult_mtrx_at_numb = []
        for el in self.list_in_class:
            mult_mtrx_at_numb.append(
                [int(numb) * other
                 for numb in el
                 ]
            )
        return Matrix(mult_mtrx_at_numb)

    __rmul__ = __mul__


exec(stdin.read())
