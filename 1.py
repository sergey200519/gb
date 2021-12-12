# 1 задание
def time(time):
    sec = time % 60
    min = int(time / 60)
    hour = int(min / 60)
    day = int(hour / 24)
    if time < 60:
        return f"{sec} сек"
    if min > 60:
        min = min % 60
    else:
        return f"{min} мин {sec} сек"
    if hour > 24:
        hour = hour % 24
    else:
        return f"{hour} час {min} мин {sec} сек"
    return f"{day} дн {hour} час {min} мин {sec} сек"


print(time(53))
print(time(153))
print(time(4153))
print(time(400153))
