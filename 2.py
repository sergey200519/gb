import json
import hashlib

login = input("Введите login он будет солью для хэша: ")
password = input("Введите password: ")

dict = {}

hash = hashlib.sha256(password.encode() + login.encode())
print(hash.hexdigest())

dict[login] = hash.hexdigest()


with open("passw.json", "w") as file:
    json.dump(dict, file, indent=4, ensure_ascii=False)


dict2 = {}
with open("passw.json", "r") as file:
    dict2 = json.load(file)

login = input("Введите login: ")
password = input("Введите password: ")

if login == list(dict2.keys())[0] and hash.hexdigest() == dict2[login]:
    print("ok")