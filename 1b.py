from datetime import datetime


def my_timer(func):
    def wrapper():
        start_time = datetime.now()
        func()
        print(datetime.now() - start_time, " time")
        return ""

    return wrapper


@my_timer
def my_dict():
    dict = {
        "one": "test1",
        "two": "test2"
    }

    dict["one"] = "test10"  # O(1)
    del dict["two"]  # O(1)
    print(dict)
    return dict


print(my_dict())


@my_timer
def l():
    l = [1, 2]
    l[0] = 3  # O(1)
    l.pop(1)  # O(n)
    print(l)
    return l


print(l())

# работа со славарём быстрее
