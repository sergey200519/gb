start = "1234"
answer = []
for item in start:
    answer.append(item)
print(answer)



n = []
def func():
    if len(answer) == 1:
        n.append(answer[0])
        return "".join(n)
    n.append(answer[-1])
    answer.pop(-1)
    return func()

print(func())