from random import randint
from timeit import timeit


def med(lst):
    for i in range(int(len(lst) / 2)):
        lst.remove(max(lst))
    return max(lst)


print(med([3, 4, 6, 2, 1]))

orig_list = [randint(-100, 100) for _ in range(11)]
# замеры 11
print(
    timeit(
        "med(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(101)]

# замеры 101
print(
    timeit(
        "med(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(1001)]

# замеры 1001
print(
    timeit(
        "med(orig_list[:])",
        globals=globals(),
        number=1000))


# Я использую длину 11 101 и 1001 так как для нахождения медианы массива нужен нечетный массив