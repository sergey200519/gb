from datetime import datetime

def my_timer(func):
    def wrapper():
        start_time = datetime.now()
        func()
        print(datetime.now() - start_time, " time")
        return ""
    return wrapper

@my_timer
def add_dict():
    dict = {}
    dict["test"] = 10 # O(1)
    return dict

print(add_dict())

@my_timer
def add_l():
    l = []
    l.append("test") # O(1)
    return l

print(add_l())

# При заполнении словаря происходит хэширования что и замедляет наш код  .