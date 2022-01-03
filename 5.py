def func(n, end, copy_end):
    if n >= 127:
        return ""
    print(f"{n} - {chr(n)}", end=" " if end > 0 else "\n")
    if end <= 0:
        end = copy_end + 1
    return func(n + 1, end - 1, copy_end)

print(func(32, 9, 9))