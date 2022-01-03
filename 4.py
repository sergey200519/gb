from hashlib import sha256


class Urls:
    def __init__(self):
        self.urls_dict = {}

    def read(self, url):
        if not self.urls_dict.get(url):  # проверка если есть такая запись
            self.urls_dict[url] = sha256(url.encode() + "salt".encode()).hexdigest()
            return self.urls_dict.get(url)
        else:
            return self.urls_dict.get(url)

    def read_dict(self):
        return self.urls_dict


test = Urls()
test.read("https://gb.ru/lessons/192647")
print(test.read_dict())
test.read("https://gb.ru/lessons/192647")
print(test.read_dict())
test.read("https://gb.ru/lessons/192648")
print(test.read_dict())
