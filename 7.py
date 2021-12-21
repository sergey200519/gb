answer = []
def func(n, t):
    if n <= 1:
        answer.append(n)
        return sum(answer) == (t*t+t*1)/2
    answer.append(n)
    return func(n - 1, t)
print(func(5, 5))