from collections import Counter
from timeit import timeit
n = int(1e6)
array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


print(func_1())
print(func_2())
print(timeit("func_1()", setup='from __main__ import func_1', number=n))
print(timeit("func_2()", setup='from __main__ import func_2', number=n))

def my_func():
     return Counter(array).most_common()[0][0]
print(my_func())
print(timeit("my_func()", setup='from __main__ import my_func', number=n))

# я использовал Counter ускорить не получилось но решение лаконичное