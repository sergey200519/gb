# 1
import random


def check_1(lst_obj):
    """Функция должна создать множество из списка.
    Алгоритм 1:
    Создать множество из списка
    Сложность: O(n).
    """
    lst_to_set = set(lst_obj)  # O(n)
    return lst_to_set  # O(1)


def check_2(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.
    Алгоритм 2:
    Проходимся по списку и для каждого элемента проверяем,
    что такой элемент отстутствует
    в оставшихся справа элементах
    Сложность: O(n).
    """
    for j in range(len(lst_obj)):  # O(n)
        if lst_obj[j] in lst_obj[j + 1:]:  # O(1)
            return False  # O(1)
    return True


def check_3(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.
    Алгоритм 3:
    Вначале выполним для списка сортировку, далее, сравниваем элементы попарно
    Если присутствуют дубли, они будут находиться рядом.
    Сложность: O(n)
    """
    lst_copy = list(lst_obj)  # O(n)
    lst_copy.sort()  # O(log n)
    for i in range(len(lst_obj) - 1):  # O(n)
        if lst_copy[i] == lst_copy[i + 1]:  # O(1)
            return False  # O(1)
    return True  # O(1)


# 2
def my_min(l):  # O(n)
    answer = l[0]
    for item in l:
        if answer > item:
            answer = item
    return answer
def my_min2(l):  # O(n^2)
    answer = l[0]
    i = 1
    while i < len(l)-1:
        temp = [l[i], l[i-1]]
        j = 0
        while j < len(temp):
            if temp[j] < answer:
                answer = temp[j]
            j += 1
        i += 1
    return answer

# 3
dict = {
    "компания 1": 10000,
    "компания 2": 13256,
    "компания 3": 14000,
    "компания 4": 164543,
    "компания 5": 3462
}
def best_company(): # O(n)
    temp = []
    answer = []
    for item in dict.items():
        temp.append(item[1])
    temp2 = sorted(temp, reverse=True)
    for item in dict.items():
        if item[1] == temp2[0] or item[1] == temp2[1] or item[1] == temp2[2]:
            answer.append([item[0], item[1]])
    return answer
def best_company2(): # O(n^2)
    temp = [["pass", -1000]]
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

# 4
data = [["sergey", 12345, "active"], ["ivan", 54321, "no_active"], ["alex", 78901, "active"]]
def entrance(log, passw): # O(n)
    answer = ""
    for item in data:
        if log == item[0] and passw == item[1]:
            if item[2] == "active":
                answer = f"Добро пожаловать {item[0]}"
                break
            else:
                answer = "Вы не актевированы"
    if answer == "":
        answer = "not found"
    return answer
def entrance2(log, passw): # O(n^2)
    answer = ""
    for item in data:
        i = 0
        while i < len(item):
            if item[i] == log and item[i + 1] == passw:
                answer = f"Добро пожаловать {item[0]}"
            if item[i] == "no_active" and item[i - 2] == log and item[i - 1] == passw:
                return f"Вы не актевированы {item[0]}"
            i += 1
    if answer == "":
        answer = "not found"
    return answer

# 5
import math
class Stack:
    def __init__(self):
        self.elements = []

    def push(self, n):
        if len(self.elements) == 0:
            i = 0
            while i < math.ceil(n / 5):
                self.elements.append([])
                i += 1
            i = 0
            while i < len(self.elements):
                if n > 5:
                    j = 0
                    while j < 5:
                        self.elements[i].append("🍽")
                        n -= 1
                        j += 1
                else:
                    while n > 0:
                        self.elements[-1].append("🍽")
                        n -= 1
                i += 1
        else:
            last_len = 5 - len(self.elements[-1])
            while last_len > 0:
                self.elements[-1].append("🍽")
                n -= 1
                last_len -= 1
            last = self.elements.index(self.elements[-1])
            print(last)
            if n % 5 == 0:
                count = n / 5
                i = 0
                while i < count:
                    self.elements.append(["🍽", "🍽", "🍽", "🍽", "🍽"])
                    i += 1
            else:
                i = 0
                while i < math.ceil(n / 5):
                    self.elements.append([])
                    i += 1
                i = last + 1
                while i < len(self.elements):
                    if n > 5:
                        j = 0
                        while j < 5:
                            self.elements[i].append("🍽")
                            n -= 1
                            j += 1
                    else:
                        while n > 0:
                            self.elements[-1].append("🍽")
                            n -= 1
                    i += 1
    def show(self):
        return self.elements
stack = Stack()
stack.push(3)
stack.push(13)
print(stack.show())

# 6
class Queue:
    def __init__(self):
        self.unsolved = []
        self.shortcomings = []
        self.solved = []
    def new_task(self, s, d):
        self.unsolved.insert(0, f"{s} {d}")
    def done(self, s, d, new_d):
        try:
            self.unsolved.remove(f"{s} {d}")
            self.solved.insert(0, f"{s} {d} {new_d}")
        except:
            print("not found")
    def remake(self, s, d, new_d, why):
        try:
            self.solved.remove(f"{s} {d} {new_d}")
            self.shortcomings.insert(0, f"{s} {d}, {why}")
        except:
            print("not found")
    def show(self):
        return f"{self.unsolved} - несделаное \n{self.shortcomings} - переделать \n{self.solved} - сделано"
queue = Queue()
queue.new_task("test1", "01/01/2021")
queue.new_task("test2", "02/01/2021")
queue.new_task("test3", "03/01/2021")
queue.new_task("test4", "04/01/2021")
queue.new_task("test5", "05/01/2021")
queue.done("test5", "05/01/2021", "07/01/2021")
queue.done("test4", "04/01/2021", "06/01/2021")
queue.remake("test5", "05/01/2021", "07/01/2021", "неправильно")
print(queue.show())












class DequeClass:
    def __init__(self):
        self.elems = []
    def is_empty(self):
        return self.elems == []
    def add_to_front(self, elem):
        self.elems.append(elem)
    def add_to_rear(self, elem):
        self.elems.insert(0, elem)
    def remove_from_front(self):
        return self.elems.pop()
    def remove_from_rear(self):
        return self.elems.pop(0)
    def size(self):
        return len(self.elems)


def pal_checker(string):
    string = string.replace(" ", "")
    dc_obj = DequeClass()
    for el in string:
        dc_obj.add_to_rear(el)
    still_equal = True
    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if first != last:
            still_equal = False
    return still_equal

print(pal_checker("молоко делили ледоколом"))
