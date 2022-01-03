from collections import OrderedDict
from timeit import timeit
from random import randrange

n = int(1e6)

let_dict = {}
dict2 = OrderedDict()

def mydict():
    let_dict[f"{randrange(1, 1000)}"] = f"{randrange(1, 1000)}"
    let_dict["abc"] = 3
    let_dict["abc"] = 1
    del let_dict["abc"]

    return let_dict


def myorderdict():
    dict2[f"{randrange(1, 1000)}"] = f"{randrange(1, 1000)}"
    dict2["abc"] = 3
    dict2["abc"] = 1
    del dict2["abc"]
    return dict2


print(timeit("mydict()", setup='from __main__ import mydict', number=n))
print(timeit("myorderdict()", setup='from __main__ import myorderdict', number=n))

# orderdict хуже dict