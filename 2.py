def from_str_to_list(s):
    return [it for it in str(s)]


def from_dec_to_hex(n):
    s = ''
    h = '0123456789ABCDEF'
    while n > 0:
        s = h[n % 16] + s
        n = n // 16
    return s


class Hex:
    def __init__(self, value):
        self.value = value

    def show(self):
        return from_str_to_list(self.value)

    def __add__(self, other):
        return Hex(from_str_to_list(from_dec_to_hex(int(self.value, 16) + int(other.value, 16))))

    def __mul__(self, other):
        return Hex(from_str_to_list(from_dec_to_hex(int(self.value, 16) * int(other.value, 16))))


a = Hex("A2")
print(a.show())
b = Hex("C4F")
c = a + b
d = a * b
print(c.value)
print(d.value)
