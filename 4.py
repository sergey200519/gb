import hashlib

class Urls():
    def __init__(self):
        self.urls_dict = {}
    def read(self, url):
        if not self.urls_dict.get(url):
            print("if")
            self.urls_dict[url] = hashlib.sha256(url.encode() + "salt".encode()).hexdigest()
            return self.urls_dict.get(url)
        else:
            print("else")
            return self.urls_dict.get(url) # hashlib.sha256(url.encode() + "salt".encode())
    def read_dict(self):
        return self.urls_dict
        
        
test = Urls()
test.read("https://gb.ru/lessons/192647")
print(test.read_dict())
test.read("https://gb.ru/lessons/192647")
print(test.read_dict())
test.read("https://gb.ru/lessons/192648")
print(test.read_dict())
