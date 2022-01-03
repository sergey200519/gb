from collections import deque
from timeit import timeit

n = int(1e1)


# 1  append, pop, extend
def mylist():
    mylist = [1, 2, 3]
    for i in range(n):
        mylist.append(4)
        mylist.pop()
        mylist.extend([4, 5])
    return mylist


def mydeque():
    mydqe = deque([1, 2, 3])
    for i in range(n):
        mydqe.append(4)
        mydqe.pop()
        mydqe.extend([4, 5])
    return mydqe


print(timeit("mylist()", setup='from __main__ import mylist', number=n))
print(timeit("mydeque()", setup='from __main__ import mydeque', number=n))
print("-" * 50 + "2" + "-" * 50)


# 2
def mylist2():
    mylist= [1, 2, 3]
    for i in range(n):
        mylist.insert(0, 0)
        mylist.pop(0)
        # аналог extendleft
        mylist.insert(0, 0)
        mylist.insert(0, - 1)
    return mylist


def mydeque2():
    mydqe = deque([1, 2, 3])
    for i in range(n):
        mydqe.appendleft(0)
        mydqe.popleft()
        mydqe.extendleft([0, -1])
    return mydqe


print(timeit("mylist2()", setup='from __main__ import mylist2', number=n))
print(timeit("mydeque2()", setup='from __main__ import mydeque2', number=n))
print("-" * 50 + "3" + "-" * 50)


# 3

def getlist():
    mylist= [1, 2, 3]
    for i in range(n):
        temp = mylist[1]
    return mylist[1]

def getdeque():
    mylist= deque([1, 2, 3])
    for i in range(n):
        temp = mylist[1]
    return mylist[1]


print(timeit("getlist()", setup='from __main__ import getlist', number=n))
print(timeit("getdeque()", setup='from __main__ import getdeque', number=n))

# 1 постепеное заполнение list быстрее
# 2 но левовое заполнение бысстрее deque
# 3 получение быстрее у list
# при n = 1e9
# 229.5025319099659
# 352.2566616679542
# --------------------------------------------------2--------------------------------------------------
# 296.15352192102
# 355.1733013159828
# --------------------------------------------------3--------------------------------------------------
# 114.7060173790087
# 216.73726600100053