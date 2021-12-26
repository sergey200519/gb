from collections import Counter
from timeit import timeit

dict = {
    "компания 1": 10000,
    "компания 2": 13256,
    "компания 3": 14000,
    "компания 4": 164543,
    "компания 5": 3462
}
test = (("компания 1", 10000),
        ("компания 2", 13256),
        ("компания 3", 14000),
        ("компания 4", 164543),
        ("компания 5", 3462)
        )
test2 = [["компания 1", 10000],
         ["компания 2", 13256],
         ["компания 3", 14000],
         ["компания 4", 164543],
         ["компания 5", 3462]
         ]


def best_company():  # O(n^2)
    temp = []
    for it in test:  # O(n)
        i = 0
        while i < it[1]:  # O(n)
            temp.append(it[0])
            i += 1
    return Counter(temp).most_common(3)


print(best_company())


# этот вариант лучше здесь меньше итераций и операций тоже меньше
def best_company2():  # O(n^2)
    temp = [["pass", -1000]]  # это заглушка
    for item in dict.items():
        for it in temp:
            if it[1] <= item[1]:
                temp.insert(temp.index(it), item)
                break
            elif temp[-1][1] > item[1]:
                temp.append(item)
                break
    return temp[:3]


print(best_company2())


def best_company3():  # O(n)
    temp = []
    for it in test2:
        temp.append(it[1])
    temp = sorted(temp)[-3:]
    temp = temp[::-1]
    temp2 = []
    for it in test2:
        temp2.append(it[0])
        temp2.append(it[1])
    answer = []
    for it in temp:
        answer.append(f"{temp2[temp2.index(it) - 1]} - {it}")
    return answer
print(best_company3())


print(timeit('best_company()', setup='from __main__ import best_company', number=100))
print(timeit('best_company2()', setup='from __main__ import best_company2', number=100))
print(timeit('best_company3()', setup='from __main__ import best_company3', number=100))
