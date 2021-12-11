import copy
from sys import stdin


class Matrix:
    def __init__(self, in_list):
        self.for_print = copy.deepcopy(in_list)

    def __str__(self):
        self.result = ''
        for el in self.for_print:
            self.result += '\t'.join([str(i) for i in el]) + '\n'
        return self.result.strip('\n')

    def size(self):
        return len(self.for_print), len(self.for_print[0])


exec(stdin.read())
