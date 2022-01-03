from memory_profiler import profile

def list_to_str(l):
    answer = ""
    for item in l:
        answer += item
    return answer


names = []

@profile
def greeting(l):
    print(l[0].split(" "))
    for item in l:
        item = item.split(" ")
        name = list(item[-1].lower())
        name[0] = name[0].upper()
        print(f"Привет {list_to_str(name)}!")
        names.append(list_to_str(name))
    return names


print(greeting(
    ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']))

@profile
def greeting2(l):
    for item in l:
        item = item.split(" ")[-1]
        item = item.lower()
        item = f"Привет {item[0].upper()}{item[1:]}!"
        print(item)
    return ""

print(greeting2(['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']))

# Убрал лишние переменные. Что и уменьшило затраты памяти