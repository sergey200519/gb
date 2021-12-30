from collections import deque
from timeit import timeit

n = int(1e6)


# 1  append, pop, extend
def mylist():
    l = [1, 2, 3]
    l.append(4)
    l.pop()
    l.extend([4, 5])
    return l


def mydeque():
    d = deque([1, 2, 3])
    d.append(4)
    d.pop()
    d.extend([4, 5])
    return d


print(timeit("mylist()", setup='from __main__ import mylist', number=n))
print(timeit("mydeque()", setup='from __main__ import mydeque', number=n))
print("-" * 50 + "2" + "-" * 50)


# 2
def mylist2():
    l = [1, 2, 3]
    l.insert(0, 0)
    l.pop(0)
    # аналог extendleft
    l.insert(0, 0)
    l.insert(0, - 1)
    return l


def mydeque2():
    d = deque([1, 2, 3])
    d.appendleft(0)
    d.popleft()
    d.extendleft([0, -1])
    return d


print(timeit("mylist2()", setup='from __main__ import mylist2', number=n))
print(timeit("mydeque2()", setup='from __main__ import mydeque2', number=n))
print("-" * 50 + "3" + "-" * 50)


# 3

def getlist():
    l = [1, 2, 3]
    return l[1]


def getdeque():
    l = deque([1, 2, 3])
    return l[1]


print(timeit("getlist()", setup='from __main__ import getlist', number=n))
print(timeit("getdeque()", setup='from __main__ import getdeque', number=n))

# постепеное заполнение list быстрее но левовое заполнение бысстрее deque получение быстрее у list
# при n = 1e9
# 229.5025319099659
# 352.2566616679542
# --------------------------------------------------2--------------------------------------------------
# 296.15352192102
# 355.1733013159828
# --------------------------------------------------3--------------------------------------------------
# 114.7060173790087
# 216.73726600100053