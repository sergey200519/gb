from memory_profiler import profile

class Clothes:
    @profile
    def __init__(self, v, h):
        self.v = v
        self.h = h

    @property
    def coat(self):
        return int(self.v / 6.5 + 0.5)

    @property
    def kostm(self):
        return int(2 * self.h + 0.3)


a = Clothes(250, 300)

print(a.coat)
print(a.kostm)


class Clothes2:
    __slots__ = ["v", "h"]

    @profile
    def __init__(self, v, h):
        self.v = v
        self.h = h

    @property
    def coat(self):
        return int(self.v / 6.5 + 0.5)

    @property
    def kostm(self):
        return int(2 * self.h + 0.3)

a = Clothes2(250, 300)

print(a.coat)
print(a.kostm)
# Я использовал слоты