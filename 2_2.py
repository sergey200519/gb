from random import randint
from timeit import timeit


def med(lst):
    for i in range(int(len(lst) / 2)):
        lst.remove(max(lst))
    return max(lst)


print(med([3, 4, 6, 2, 1]))

orig_list = [randint(-100, 100) for _ in range(10)]
# замеры 10
print(
    timeit(
        "med(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit(
        "med(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit(
        "med(orig_list[:])",
        globals=globals(),
        number=1000))

