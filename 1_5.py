from memory_profiler import profile

import math
@profile
def price(l, categories=None):
    for item in l:
        i = l.index(item)
        if type(item) == float:
            whole_part = str(math.floor(item)).zfill(2)
            part = str(round(item - int(whole_part), 2)).zfill(5)
            l[i] = float(f"{whole_part}.{part[2:].replace('.', '')}")
            print(f"{whole_part} руб, {part[2:].replace('.', '')} коп")
        else:
            ruble = str(item).zfill(2)
            l[i] = int(ruble)
            print(f"{ruble} руб")
    return l
product = [57.8, 46.51, 97, 55, 55.5, 15.3, 0.3, 10, 100.5, 1000, 1, 2, 03.33]
print(price(product))

@profile
def price2(l):
    answer = []
    for item in l:
        num = str(item).split(".")
        if type(item) == float:
            answer.append(f"{'0' if len(num[0]) == 1 else ''}{num[0]}руб, {'0' if len(num[-1]) == 1 else ''}{num[-1]}коп")
        else:
            answer.append(f"{'0' if len(num[0]) == 1 else ''}{num[0]}руб")
    return answer

print(price2(product))


# Из использования Тернарного оператора уменьшилось количество ненужных переменных (whole_part, part, ruble, i)