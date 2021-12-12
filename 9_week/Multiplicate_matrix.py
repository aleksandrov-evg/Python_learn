import copy
from sys import stdin


class MatrixError(BaseException):
    def __init__(self, matrix_1, sec_arg):
        self.matrix1 = matrix_1
        self.matrix2 = sec_arg


class Matrix:
    def __init__(self, in_list):
        self.matrix = copy.deepcopy(in_list)

    def __str__(self):
        self.result = ''
        for el in self.matrix:
            self.result += '\t'.join([str(i) for i in el]) + '\n'
        return self.result.strip('\n')

    def size(self):
        return len(self.matrix), len(self.matrix[0])

    def __add__(self, other):
        first = self.matrix
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

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            mult_mtrx_at_numb = []
            for el in self.matrix:
                mult_mtrx_at_numb.append(
                    [numb * other
                     for numb in el
                     ]
                )
            return Matrix(mult_mtrx_at_numb)
        elif isinstance(other,
                        Matrix):
            mult_mtrx = self.matrix
            for ls in range(len(self.matrix)):
                for el in range(len(self.matrix[ls])):
                    mult_mtrx[ls][el] *= other.matrix[ls][el]
            return Matrix(mult_mtrx)
        else:
            raise MatrixError(self, other)

    __rmul__ = __mul__

    def make_transpose(self):
        new_obj = []
        for p_l in range(len(self.matrix[0])):
            tmp = []
            for p_g in range(len(self.matrix)):
                tmp.append(self.matrix[p_g][p_l])
            new_obj.append(tmp)
        return new_obj

    def transpose(self):
        self.matrix = self.make_transpose()
        return Matrix(self.matrix)

    def transposed(self):
        return Matrix(self.make_transpose())

    def check_mtrx(self, other):
        first = [''.join(str(len(x))) for x in self.matrix]
        second = [''.join(str(len(y))) for y in other.matrix]
        return first == second


# exec(stdin.read())
mid = Matrix([[1, 0, 0],[0, 1, 0],[0, 0, 1]])
print(mid)
print(mid.size())
m1 = Matrix([[3, 2], [-10, 0], [14, 5]])
print(m1)
print(m1.size())
m2 = Matrix([[5, 2, 10], [-0.5, -0.25, 18], [-22, -2.5, -0.125]])
print(mid * m1)
print(mid * m2)
print(m2 * m1)
try:
    m = m1 * m2
    print("WA It should be error")
except MatrixError as e:
    print(e.matrix1)
    print(e.matrix2)
