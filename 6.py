import random, math
def func():
    n = math.floor(random.randrange(0, 100))
    # print(n) for testing
    main = input("Введите число: ")
    if int(main) == n:
        return "win"
    print(f"False {n}")
    return func()
func()