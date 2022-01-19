from random import randint
from timeit import timeit


def bubble_sort(lst_obj):
    n = 1
    flag = True
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i+1], lst_obj[i] = lst_obj[i], lst_obj[i+1]
                flag = False
        if flag:
            return lst_obj
        n += 1
    return lst_obj


orig_list = [randint(1, 10) for _ in range(10)]
print(bubble_sort(orig_list[:]))
print(
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))


# Условия о совершение замены помогает если масив небольшой