from collections import OrderedDict


def test():
    n = int(input("Введите количество предприятия: "))
    companies = OrderedDict()
    average = 0
    names = []
    i = 0
    while i < n:
        names.append(input("Введите название предприятия: "))
        companies[names[-1]] = {
            "p_1": int(input("Введите прибыль за первый квартал: ")),
            "p_2": int(input("Введите прибыль за второй квартал: ")),
            "p_3": int(input("Введите прибыль за третий квартал: ")),
            "p_4": int(input("Введите прибыль за четвёртый квартал: "))
        }
        average += (companies[names[-1]]["p_1"] + companies[names[-1]]["p_2"] + companies[names[-1]]["p_3"] +
                    companies[names[-1]]["p_4"])
        i += 1
    average = average / (n * 4)
    best = []
    worst = []
    for item in names:
        if companies[item]["p_1"] + companies[item]["p_2"] + \
                companies[item]["p_3"] + companies[item]["p_4"] > average:
            best.append(item)
        else:
            worst.append(item)
    return f"{best} - выше среднего \n{worst} - ниже среднего \n{average} - средние значение"


print(test())
