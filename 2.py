start = "1234"
answer = []
for item in start:
    answer.append(item)
print(answer)


def func(e, o):
    if len(answer) == 1:
        if int(answer[0]) % 2 == 0:
            e += 1
        else:
            o += 1
        return f"{e} - чётных, {o} - нечётных"
    if int(answer[0]) % 2 == 0:
        e += 1
    else:
        o += 1
    answer.pop(0)
    return func(e, o)

print(func(0, 0))