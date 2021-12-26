data = [["sergey", 12345, "active"], ["ivan", 54321, "no_active"], ["alex", 78901, "active"]]


def entrance(log, passw):  # O(n)
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


def entrance2(log, passw):  # O(n^2)
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


users = {
    "sergey": {"password": 123, "active": True},
    "sergey1": {"password": 123, "active": False}
}


def entrance3(log, passw):  # O(1)
    if users.get(log):
        if users[log]["password"] == passw and users[log]["active"]:
            return "Welcome"
        elif users[log]["password"] == passw and not users[log]["active"]:
            return "not active"
        elif users[log]["password"] != passw:
            return "ERROR password"
    else:
        return "ERROR user not"


print(entrance3("sergey1", 123))
print(entrance3("sergey", 123))
print(entrance3("segey", 123))
