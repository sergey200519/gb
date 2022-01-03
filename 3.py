def func(answer, n=""):
    if len(str(answer)) == 1:
        n += str(answer)
        return int(n)
    temp = str(answer % 10)
    n += temp
    answer = answer // 10
    return func(answer, n)

print(func(1234))