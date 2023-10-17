

import math
try:
    print("Добро пожаловать в калькулятор!")
    print("\nОперации: сложение, вычитание, умножение, деление, корень числа, возведение в степень")
    print("факториал, синус, косинус, тангенс")
    s = input("Введите название выбранной операции (так как она написана), или ее знак ")

    if s == 'сложение' or s == '+':
        def add(mk, d):
            result = mk + d
            return result
        a = float(input("введите первое слагаемое "))
        b = float(input("введите второе слагаемое "))
        c = add(a, b)
        print("результат", c)

    elif s == 'вычитание' or s == '-':
        def minus(mk, d):
            result = mk - d
            return result
        a = float(input("введите уменьшаемое "))
        b = float(input("введите вычитаемое "))
        c = minus(a, b)
        print("результат", c)

    elif s == "умножение" or s == '*':
        def multiply(mk, d):
            result = mk*d
            return result
        a = float(input("введите первый множитель "))
        b = float(input("введите второй множитель "))
        c = multiply(a, b)
        print("результат", c)

    elif s == "деление" or s == "/":
        def div(mk, d):
            result = mk/d
            return result
        a = float(input("введите делимое "))
        b = float(input("введите делитель "))

        if b != 0:
            c = div(a, b)
            print("результат", c)
        if b == 0:
            print("Деление на ноль невозможно.")

    elif s == "корень числа" or s == "√":
        def root(mk, d):
            result = pow(d, 1./mk)
            return result
        a = float(input("введите степень корня "))
        b = float(input("введите число под корнем "))
        c = root(a, b)
        print("результат", c)

    elif s == "возведение в степень" or s == "^":
        def expo(mk, d):
            result = pow(d, mk)
            return result
        a = float(input("введите степень корня "))
        b = float(input("введите число, возводимое в степень "))
        c = expo(a, b)
        print("результат", c)

    elif s == "факториап" or s == "!":
        def facc(mk):
            if mk == 1:
                return 1
            result = facc(mk - 1) * mk
            return result

        a = int(input("введите число, факториал которого вы хотите найти"))
        if a > 21:
            print("Простите, данная программа не может высчитать факториал числа, большего 21")
        else:
            c = facc(a)
            print("результат", c)

    elif s == "sin" or s == "синус":
        def sin(mk):
            result = math.sin(mk)
            return result
        a = float(input("Введите градусное значение угла, синус которого вы хотите найти"))
        c = sin(a)
        print("синус равен", c)

    elif s == "cos" or s == "косинус":
        def cos(mk):
            result = math.cos(mk)
            return result
        a = float(input("Введите градусное значение угла, косинус которого вы хотите найти"))
        c = cos(a)
        print("косинус равен", c)

    elif s == "tg" or s == "tan" or s == "тангенс":
        def tan(mk):
            result = math.tan(mk)
            return result
        a = float(input("Введите градусное значение угла, тангенс которого вы хотите найти"))
        c = tan(a)
        print("тангенс равен", c)
except ValueError:
    print("Введенное значение не было числом/не могло быть воспринято программой как число.")
