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

print(shell_sort([3,4,6,2,1]))

orig_list = [randint(-100, 100) for _ in range(11)]
# замеры 11
print(
    timeit(
        "shell_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(101)]

# замеры 101
print(
    timeit(
        "shell_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(1001)]

# замеры 1001
print(
    timeit(
        "shell_sort(orig_list[:])",
        globals=globals(),
        number=1000))


# Я использую длину 11 101 и 1001 так как для нахождения медианы массива нужен нечетный массив