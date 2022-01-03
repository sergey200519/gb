import random, math

def func(c):
    n = math.floor(random.randrange(0, 100))
    # print(n) for testing
    main = input("Введите число: ")
    if c <= 1:
        if int(main) == n:
            return "win"
        else:
            return

    if int(main) == n:
        return "win"
    print(f"False {n}")
    return func(c - 1)
func(10)

if __name__ == '__main__':
    pass