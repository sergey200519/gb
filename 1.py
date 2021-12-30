from collections import namedtuple

def test():
    n = int(input("Введите количество предприятия: "))
    main = "company"
    comanies = namedtuple(main, "name p1 p2 p3 p4")
    data = {}
    average = 0
    i = 0
    while i < n:
        p_1 = int(input("Введите прибыль за первый квартал: "))
        p_2 = int(input("Введите прибыль за второй квартал: "))
        p_3 = int(input("Введите прибыль за третий квартал: "))
        p_4 = int(input("Введите прибыль за четвёртый квартал: "))
        company = comanies(name=input("Введите название предприятия: "), p1=p_1, p2=p_2, p3=p_3, p4=p_4)
        data[company.name] = (company.p1 + company.p2 + company.p3 + company.p4) / 4
        average += (company.p1 + company.p2 + company.p3 + company.p4) / 4
        i += 1

    average = average
    best = []
    worst = []
    for key, value in data.items():
        if value > average:
            best.append(key)
        else:
            worst.append(key)

    return f"{best} - выше среднего \n{worst} - ниже среднего \n{average} - средние значение"

print(test())