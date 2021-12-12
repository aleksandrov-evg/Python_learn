import copy
from sys import stdin


class MatrixError(BaseException):
    def __init__(self, matrix_1, matrix_2):
        self.matrix1 = Matrix(matrix_1)
        self.matrix2 = Matrix(matrix_2)


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
        second = other.matrix
        add_f_s = []
        if len(first) == len(second):
            for i in range(len(first)):
                add_f_s.append(
                    [first[i][x] + second[i][x]
                     for x in range(len(first[i]))]
                )
            return Matrix(add_f_s)
        else:
            raise MatrixError(first, second)

    '''def __mul__(self, other):
        if isinstance(other, int or float):
            mult_mtrx_at_numb = []
            for el in self.list_in_class:
                mult_mtrx_at_numb.append(
                    [int(numb) * other
                     for numb in el
                     ]
                )
            return Matrix(mult_mtrx_at_numb)'''

    def __mul__(self, other):

        for i in range(len(m1)):
            for j in range(len(m2[0])):
                sums = 0
                for k in range(len(m2)):
                    sums = sums + (m1[i][k] * m2[k][j])
                r.append(sums)
            m.append(r)
            r = []
        return m

    __rmul__ = __mul__

    def make_transpose(self):
        new_obj = []
        for pos_in_list in range(len(self.list_in_class[0])):
            tmp = []
            for pos_in_group in range(len(self.list_in_class)):
                tmp.append(self.list_in_class[pos_in_group][pos_in_list])
            new_obj.append(tmp)
        return new_obj

    def transpose(self):
        self.list_in_class = self.make_transpose()
        return Matrix(self.list_in_class)

    def transposed(self):
        return Matrix(self.make_transpose())


exec(stdin.read())
