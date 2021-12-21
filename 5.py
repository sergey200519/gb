def func(n, end, copy_end):
    if n >= 127:
        return ""
    if end > 0:
        print(f"{n} - {chr(n)}", end=" ")
    else:
        print(f"{n} - {chr(n)}", end="\n")
        end = copy_end + 1
    return func(n + 1, end - 1, copy_end)

print(func(32, 9, 9))