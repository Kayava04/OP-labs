#  Варіант 3


from random import choice
from colorama import init, Fore
init()
print(Fore.CYAN)



main_menu = ["Завдання 1", "Завдання 2", "Вихід(Х)"]
exercises = ["Вправа 1", "Вправа 2", "Вправа 3"]
dop_menu = ["1. Продовжити", "0. Повернутися назад"]


#  Завдання 1


def clock():
    hour = int(input("Введіть лише години: "))
    minute = int(input("Введіть лише минути: "))
    res = abs((hour % 12 * 30 - minute * 5.5))
    print(f"Результат: {res} градусів")
    dop_menu_1()


#  Завдання 2


def exrcise_1():
    A = int(input("Введіть A: "))
    B = int(input("Введіть B: "))

    if A != 0 and B != 0:
        if A == B:
            print("Квадрат")
        else:
            print("Прямокутник")
    else:
        if A == 0 and B == 0:
            print("Точка")
        else:
            print("Відрізок")

def exrcise_2():
    x1 = int(input("Введіть x1: "))
    x2 = int(input("Введіть x2: "))
    x3 = int(input("Введіть x3: "))
    x4 = int(input("Введіть x4: "))
    x5 = int(input("Введіть x5: "))

    m = x1  # Початкове максимальне значення
    k = 0  # Кількість чисел

    if x2 > m:
        m = x2
    if x3 > m:
        m = x3
    if x4 > m:
        m = x4
    if x5 > m:
        m = x5

    if m == x1:
        k += 1
    if m == x2:
        k += 1
    if m == x3:
        k += 1
    if m == x4:
        k += 1
    if m == x5:
        k += 1

    print(f"Кількість елементів, що відповідають максимальному значенню: {k}")

def exercise_3():
    a1 = int(input("Введіть a1: "))
    a2 = int(input("Введіть a2: "))
    a3 = int(input("Введіть a3: "))
    a4 = int(input("Введіть a4: "))
    a5 = int(input("Введіть a5: "))

    b1 = int(input("Введіть b1: "))
    b2 = int(input("Введіть b2: "))
    b3 = int(input("Введіть b3: "))
    b4 = int(input("Введіть b4: "))
    b5 = int(input("Введіть b5: "))

    k = 0  # Кількість чисел для значення A
    n = 0  # Кількість чисел для значення B

    if a1 > b1:
        k += 1
    if a2 > b2:
        k += 1
    if a3 > b3:
        k += 1
    if a4 > b4:
        k += 1
    if a5 > b5:
        k += 1

    if b1 > a1:
        n += 1
    if b2 > a2:
        n += 1
    if b3 > a3:
        n += 1
    if b4 > a4:
        n += 1
    if b5 > a5:
        n += 1

    print(f"Кількість чисел A, що перебільшують B: {k}")
    print(f"Кількість чисел B, що перебільшують A: {n}")

def exercisess():
    for i in range(len(exercises)):
        print(i + 1, ". ", exercises[i], sep = "")
    print()
    choice_2 = int(input("Виберіть номер вправи: "))
    if choice_2 == 1:
        print()
        exrcise_1()
    elif choice_2 == 2:
        print()
        exrcise_2()
    elif choice_2 == 3:
        print()
        exercise_3()
    dop_menu_2()

def dop_menu_1():
    print()
    for i in range(len(dop_menu)):
        print(dop_menu[i])
    print()
    choice = int(input("Виберіть пункт: "))
    print()
    if choice == 1:
        clock()
    elif choice == 0:
        menu()

def dop_menu_2():
    print()
    for i in range(len(dop_menu)):
        print(dop_menu[i])
    print()
    choice = int(input("Виберіть пункт: "))
    print()
    if choice == 1:
        exercisess()
    elif choice == 0:
        menu()

def ramka(name, symbol):
    l = len(name)
    s = symbol
    print(s * (25 + l), s, sep = "")
    print(s, " " * (24 + l), s, sep = "")
    print(s, " " * 12, name, " " * 12, s, sep = "")
    print(s, " " * (24 + l), s, sep = "")
    print(s * (25 + l), s, sep = "")

def menu():
    ramka("Лабораторна робота 1", "#")
    print()
    for i in range(len(main_menu) - 1):
        print(i + 1, ".  ", main_menu[i], sep = "")
    print("0.  ", main_menu[len(main_menu) - 1], sep = "")
    print()
    choice = int(input("Вкажіть пункт: "))
    print()
    if choice == 1:
        clock()
    elif choice == 2:
        exercisess()
    elif choice == 0:
        print("Ви успішно вийшли!")
        quit()


if __name__ == "__main__":
    menu()