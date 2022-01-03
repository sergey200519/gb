def func(answer, e, o):
    if len(str(answer)) == 1:
        if answer % 2 == 0:
            e += 1
        else:
            o += 1
        return f"{e} - чётных, {o} - нечётных"
    temp = answer % 10
    if temp % 2 == 0:
        e += 1
    else:
        o += 1
    answer =answer // 10
    return func(answer, e, o)

print(func(1234, 0, 0))