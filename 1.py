def calc():
    main = input("Введите знак: ")
    if main == "0":
        return ""
    n_one = float(input("Введите первое число: "))
    n_two = float(input("Введите второе число: "))
    if main == "+":
        print(n_one + n_two)
    elif main == "-":
        print(n_one - n_two)
    elif main == "*":
        print(n_one * n_two)
    elif main == "/":
        if n_two != 0:
            print(n_one / n_two)
        else:
            print("На нуль делить нельзя")
    else:
        print("command  not found")
    return calc()
calc()