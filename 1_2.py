from memory_profiler import profile
from gc import get_threshold, collect


def list_to_str(list):
    answer = ""
    n = len(list)
    i = 0
    while i < n:
        if list[i] == "\"":
            if len(list[i + 1]) == 1:
                answer += f"{list[i]}0{list[i + 1]}\" "
                i += 3
            else:
                answer += f"{list[i]}{list[i + 1]}\" "
                i += 3
        else:
            answer += list[i] + " "
            i += 1
    return answer
@profile
def from_list_to_str(l):
    key = []
    for item in l:
        i = l.index(item)
        if item.isdigit():
            key.append(i)
            if len(l[i]) == 1:
                l[i] = f"0{l[i]}"
        if item[0] == "+" or item[0] == "-":
            key.append(i)
            if len(l[i]) == 2:
                l[i] = f"{l[i][0]}0{l[i][1]}"
    shift = 0
    for item in key:
        l.insert(item + shift, "\"")
        shift += 1
        l.insert(item + 1 + shift, "\"")
        shift += 1
    return  list_to_str(l)

print(from_list_to_str(['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']))
get_threshold()
collect()

@profile
def from_list_to_str2(l):
    answer = ''
    for item in l:
        if item[0] == "+" or item[0] == "-":
            answer += f"\"{item[0]}{'0' if len(item) == 2 else ''}{item.replace('+' or '-', '')}\" "
        elif item.isdigit():
            answer += f"\"{'0' if len(item) == 1 else ''}{item}\" "
        else:
            answer += f"{item} "
    return answer


print(from_list_to_str2(['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']))


# Отказался от второстепенных функций написанных мной пользу встроенных