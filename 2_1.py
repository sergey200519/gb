import math
from random import randint
from timeit import timeit



def shell_sort(lst):
    n = len(lst)
    k = int(math.log2(n))
    interval = 2 ** k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = lst[i]
            j = i
            while j >= interval and lst[j - interval] > temp:
                lst[j] = lst[j - interval]
                j -= interval
            lst[j] = temp
        k -= 1
        interval = 2 ** k - 1
    return lst[int(len(lst)/2)]


orig_list = [randint(-100, 100) for _ in range(10)]
print(orig_list)
# замеры 10
print(
    timeit(
        "shell_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit(
        "shell_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit(
        "shell_sort(orig_list[:])",
        globals=globals(),
        number=1000))
