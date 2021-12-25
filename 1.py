from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

print(func_1([6, 2, 3, 8, 9, 7, 10]))
n = int(1e7)
print(timeit("func_1([6, 2, 3, 8, 9, 7, 10])", setup="from __main__ import func_1", number=n))





def myfunc(num):
    return [i for i, item in enumerate(num) if item % 2 == 0]

print(myfunc([6, 2, 3, 8, 9, 7, 10]))

print(timeit("myfunc([6, 2, 3, 8, 9, 7, 10])", setup="from __main__ import myfunc", number=n))

# я сделал генератор и время работы сократилось