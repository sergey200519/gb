import json
from hashlib import sha256

dict = {}


def func_login():
    login = input("Введите login он будет солью для хэша: ")
    password = input("Введите password: ")
    hash = sha256(password.encode() + login.encode())
    return (login, hash)

data = func_login()
dict[data[0]] = data[1].hexdigest()

with open("passw.json", "w") as file:
    json.dump(dict, file, indent=4, ensure_ascii=False)

with open("passw.json", "r") as file:
    dict2 = json.load(file)

data = func_login()

if data[0] == list(dict2.keys())[0] and data[1].hexdigest() == dict2[data[0]]:
    print("ok")
else:
    print("error")
