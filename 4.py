def func(n, old, new_n, status):
    print(new_n, n)
    if n <= 1:
        return
    return func(n - 1, new_n, old / 2 if status else old / -2, False if status else True)


print(func(5, 1, -0.5, True))