from collections import deque


def from_str_to_list(s):
    return deque(it for it in str(s))


def from_dec_to_hex(num):
    s = ''
    h = '0123456789ABCDEF'
    while num > 0:
        s = h[num % 16] + s
        num = num // 16
    return from_str_to_list(s)


a = from_dec_to_hex(16)
b = from_dec_to_hex(12)

def mysum(first, second):
    return from_dec_to_hex(int("".join(first), 16) + int("".join(second), 16))

print(mysum(a, b))