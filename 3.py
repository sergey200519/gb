from timeit import timeit
n = int(1e6)


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)

print(timeit("revers(100)", setup='from __main__ import revers', number=n))

def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num
print(timeit("revers_2(100)", setup='from __main__ import revers_2', number=n))

def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num
print(timeit("revers_3(100)", setup='from __main__ import revers_3', number=n))

def myrevers(num):
    num = list(reversed(str(num)))
    answer = ""
    for it in num:
        answer += it
    return str(answer)
print(myrevers(100))

print(timeit("myrevers(100)", setup='from __main__ import myrevers', number=n))

# самый быстрый вариант это срез он для этого и рачитан
