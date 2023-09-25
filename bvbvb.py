

import math

print("Добро пожаловать в калькулятор!")
print("\nОперации: сложение, вычитание, умножение, деление, корень числа, возведение в степень")
print("факториал, синус, косинус, тангенс")
s = input("Введите название выбранной операции (так как она написана), или ее знак ")

if s == 'сложение' or s == '+':
    a = float(input("введите первое слагаемое "))
    b = float(input("введите второе слагаемое "))
    if a == ValueError or b == ValueError or a == "" or b == "":
        print("sorry! not possible")
    else:
        c = a + b
        print("result", c)

elif s == 'вычитание' or s == '-':
    a = float(input("введите уменьшаемое "))
    b = float(input("введите вычитаемое "))
    if a == ValueError or b == ValueError or a == "" or b == "":
        print("sorry! not possible")
    else:
            c = a - b
            print("результат", c)


elif s == "умножение" or s == '*':
    a = float(input("введите первый множитель "))
    b = float(input("введите второй множитель "))
    if a == ValueError or b == ValueError or a == "" or b == "":
        print("sorry! not possible")
    else:
        c = a * b
        print("результат", c)


elif s == "деление" or s == "/":
    a = float(input("введите делимое "))
    b = float(input("введите делитель "))
    if a == ValueError or b == ValueError or a == "" or b == "":
        print("sorry! not possible")
    else:
        c = a / b
        print("результат", c)


elif s == "корень числа" or s == "√":
    a = float(input("введите степень корня "))
    b = float(input("введите число под корнем "))
    if a == ValueError or b == ValueError or a == "" or b == "":
        print("sorry! not possible")
    else:
        c = pow(b, 1./a)
        print("результат", c)


elif s == "возведение в степень" or s == "^":
    a = float(input("введите степень корня "))
    b = float(input("введите число, возводимое в степень "))
    if a == ValueError or b == ValueError or a == "" or b == "":
        print("sorry! not possible")
    else:
        c = pow(b, a)
        print("результат", c)


elif s == "факториал" or s == "!":
    a = int(input("введите число, факториал которого вы хотите найти"))
    if a == ValueError or a == "":
        print("sorry! not possible")
    else:
        factorial = 1
        while a > 1:
            factorial *= a
            a -= 1
        print("результат", factorial)


elif s == "sin" or s == "синус":
    a = float(input("Введите градусное значение угла, синус которого вы хотите найти "))
    if a == ValueError or a == "":
        print("sorry! not possible")
    else:
        print("результат ")
        print(math.sin(math.degrees(a)))


elif s == "cos" or s == "косинус":
    a = float(input("Введите градусное значение угла, косинус которого вы хотите найти "))
    if a == ValueError or a == "":
        print("sorry! not possible")
    else:
        print("результат ")
        print(math.cos(math.degrees(a)))


elif s == "tg" or s == "tan" or s == "тангенс":
    a = float(input("Введите градусное значение угла, тангенс которого вы хотите найти "))
    if a == ValueError or a == "":
        print("sorry! not possible")
    else:
            print("результат ")
            print(math.tan(math.degrees(a)))

elif s == "" or s == ValueError:
    print("sorry. pick an operation")



