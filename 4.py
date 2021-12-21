def func(n, old, new_n, status):
    print(new_n, n)
    if n <= 1:
        return
    if status:
        return func(n - 1, new_n, old / 2, False)
    else:
        return func(n - 1, new_n, old / -2, True)


print(func(5, 1, -0.5, True))