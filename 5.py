import math


# эту задачу я разделил на подзадачи

def my_list(n, letter):  # эта фунуция заполняет list
    answer = []
    while n > 0:
        answer.append(letter)
        n -= 1
    return answer


def full_list(n, count, letter):  # эта функия берёт масивы и собирает в нужном порядке
    total_answer = []
    n_list = math.floor(n / count)
    while n_list > 0:
        total_answer.append(my_list(count, letter))
        n_list -= 1
    if n - (math.floor(n / count) * count) > 0:
        answer = []
        n_item = math.ceil(n - ((math.floor(n / count)) * count))
        while n_item > 0:
            answer.append(letter)
            n_item -= 1
        total_answer.append(answer)
    return total_answer


# print(full_list(16, 5))


class Stack:
    def __init__(self):
        self.count = 5
        self.elements = []
        self.letter = "🍽"

    def push(self, n):
        if self.elements == [] or len(self.elements[-1]) == self.count:
            answer = full_list(n, self.count, self.letter)
            for it in answer:
                self.elements.append(it)
        elif len(self.elements[-1]) < self.count:
            rest = self.count - len(self.elements[-1])  # остаток сколько остлось заполнить последний list
            n -= rest
            while rest > 0:
                self.elements[-1].append(self.letter)  # заолняем последний list
                rest -= 1
            answer = full_list(n, self.count, self.letter)
            for it in answer:
                self.elements.append(it)

    def show(self):
        return self.elements


stack = Stack()
stack.push(5)
stack.push(8)
stack.push(2)
print(stack.show())
