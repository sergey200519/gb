from numpy import array, concatenate
from memory_profiler import profile

def equality_list(l):
    n = len(l[0])
    for item in l:
        if len(item) != n:
            return False
        for it in item:
            if type(it) != int:
                return False
    return True


def str_to_list(other):
    num = []
    answer = []
    old = ""
    while True:
        if other != old:
            answer.append(str(other))
            old = other
        else:
            break
    answer = answer[0].split("\n")
    del answer[-1]
    other_list = []
    for item in answer:
        other_list.append(item.split(","))
    for item in other_list:
        for it in item:
            it = it.replace("[", "")
            it = int(it.replace("]", ""))
            num.append(it)
    return num


def divisor(l, n):
    temp = []
    answer = []
    i = 0
    for item in l:
        temp.append(item)
        i += 1
        if i >= n:
            i = 0
            answer.append(temp)
            temp = []
    return answer


class Matrix:
    mat = ""
    n = 0

    @profile
    def __init__(self, mat):
        self.n = len(mat[0])
        if equality_list(mat):
            for item in mat:
                self.mat += str(item) + "\n"
        else:
            print("ошибка :)")

    def __str__(self):
        return str(self.mat)

    @profile
    def __add__(self, other):
        answer = []
        sums = zip(str_to_list(other), str_to_list(self.mat))
        for item in sums:
            answer.append(sum(item))
        answer = divisor(answer, self.n)
        return Matrix(answer)


a = Matrix([[1, 2, 3], [2, 3, 4]])
d = Matrix([[1, 2, 4], [2, 3, 5]])
sums = a + d
# print(sums)
# print(a)
# print(b)


# --------------------------------------------------------------


class Matrix2:
    __slots__ = ["mat", "flag"]

    @profile
    def __init__(self, mat, flag=True):
        if flag and not equality_list(mat):
            print("ошибка :)")
            exit()
        self.mat = mat

    def __str__(self):
        return str(self.mat)

    def get_value(self):
        return list(self.mat)

    @profile
    def __add__(self, other):
        try:
            return Matrix2(array(self.mat) + array(other.get_value()).tolist(), False)
        except:
            print("ошибка :)")


a = Matrix2([[1, 2], [3, 4]])
b = Matrix2([[1, 2], [3, 4]])
d = a + b
print(d)

# Использовал хорошо оптимизированую библиотеку numpy.
