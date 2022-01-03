from memory_profiler import profile

@profile
def thesaurus(*s):
    answer = {}
    letters = []
    for item in s:
        letter = item[0]
        if letter not in letters:
            letters.append(letter)
            answer[letter] = []
    for item in s:
        answer[item[0]].append(item)
    return answer
print(thesaurus("Иван", "Мария", "Петр", "Илья"))

@profile
def thesaurus2(*s):
    answer = {}
    letters = set()
    for item in s:
        if item[0] not in letters:
            letters.add(item[0])
            answer[item[0]] = [item]
        else:
            answer[item[0]].append(item)
    return answer
print(thesaurus2("Иван", "Мария", "Петр", "Илья"))


# Я избавился от второго цикла и вместо лист сделал множество так как множество задействует меньше памяти